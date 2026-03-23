"""Function-level fingerprint aggregated from block value signatures."""

from collections import defaultdict
import hashlib
import struct

import networkx as nx
import numpy as np

from rustdiff.micro_exec.value_signature import BlockValueSignature


class FunctionFingerprint:
    """Aggregated fingerprint for a single function.

    Combines block-level value signatures weighted by CFG structural
    properties (loop membership, dominance, convergence) into a
    function-level representation for cross-binary matching.
    """

    def __init__(self, func_addr: int, func_name: str,
                 block_sigs: dict[int, BlockValueSignature],
                 cfg: nx.DiGraph):
        self.func_addr = func_addr
        self.func_name = func_name
        self.block_sigs = block_sigs
        self.cfg = cfg
        self.num_blocks = len(block_sigs)
        self.num_instructions = sum(
            bs.num_instructions for bs in block_sigs.values()
        )
        self._weights = self._compute_block_weights()

    def _compute_block_weights(self) -> dict[int, float]:
        """Compute structural weight for each block in the CFG.

        Higher weight for:
        - Loop headers (detected via back-edges)
        - Blocks with high in-degree (convergence points)
        - Blocks with complex arithmetic
        Lower weight for:
        - Prologue/epilogue-like blocks (only push/pop/mov/ret)
        - Blocks with 0-1 instructions
        """
        weights = {}
        if not self.cfg.nodes:
            return weights

        # Detect loop headers via back-edges in DFS
        loop_headers = set()
        if self.cfg.nodes:
            try:
                for u, v in nx.dfs_edges(self.cfg):
                    # Back edge: v dominates u or v was visited before
                    if v in nx.ancestors(self.cfg, u) or v == list(self.cfg.nodes)[0]:
                        loop_headers.add(v)
            except nx.NetworkXError:
                pass

        for addr in self.block_sigs:
            w = 1.0

            # Boost loop headers
            if addr in loop_headers:
                w *= 2.0

            # Boost convergence points (high in-degree)
            if addr in self.cfg:
                in_deg = self.cfg.in_degree(addr)
                if in_deg > 1:
                    w *= 1.0 + 0.3 * (in_deg - 1)

            sig = self.block_sigs[addr]

            # Boost blocks with substantive computation
            non_trivial_ops = {'add', 'sub', 'mul', 'div', 'xor', 'and',
                               'or', 'shl', 'shr', 'cmp', 'lea'}
            op_set = set(sig.opcode_sequence)
            if op_set & non_trivial_ops:
                w *= 1.5

            # Dampen trivial blocks
            if sig.num_instructions <= 1:
                w *= 0.3
            elif set(sig.opcode_sequence) <= {'push', 'pop', 'mov', 'ret', 'nop'}:
                w *= 0.5

            weights[addr] = w

        # Normalize weights so they sum to 1
        total = sum(weights.values())
        if total > 0:
            weights = {k: v / total for k, v in weights.items()}

        return weights

    def get_constant_multiset(self) -> dict[int, float]:
        """Weighted multiset of constants across all blocks."""
        result = defaultdict(float)
        for addr, sig in self.block_sigs.items():
            w = self._weights.get(addr, 1.0)
            for c in sig.constants:
                result[c] += w
        return dict(result)

    def get_opcode_histogram(self) -> dict[str, float]:
        """Weighted histogram of normalized opcodes."""
        result = defaultdict(float)
        for addr, sig in self.block_sigs.items():
            w = self._weights.get(addr, 1.0)
            for op in sig.opcode_sequence:
                result[op] += w
        return dict(result)

    def get_memory_pattern_summary(self) -> dict:
        """Summary of memory access patterns across the function."""
        stack_reads = 0
        stack_writes = 0
        global_reads = 0
        global_writes = 0
        distinct_stack_offsets = set()
        max_stack_depth = 0

        for sig in self.block_sigs.values():
            from rustdiff.micro_exec.value_signature import ValueKind
            for ma in sig.memory_pattern:
                if ma.kind == ValueKind.STACK_OFFSET:
                    if ma.is_write:
                        stack_writes += 1
                    else:
                        stack_reads += 1
                    distinct_stack_offsets.add(ma.offset)
                    max_stack_depth = max(max_stack_depth, abs(ma.offset))
                elif ma.kind == ValueKind.GLOBAL_ADDR:
                    if ma.is_write:
                        global_writes += 1
                    else:
                        global_reads += 1

        return {
            'stack_reads': stack_reads,
            'stack_writes': stack_writes,
            'global_reads': global_reads,
            'global_writes': global_writes,
            'distinct_stack_offsets': len(distinct_stack_offsets),
            'max_stack_depth': max_stack_depth,
        }

    def get_concrete_value_vector(self) -> tuple[int, ...]:
        """Aggregate concrete output values across all blocks.

        Sorted and deduplicated. This is the analog of vSim's
        expression concretization vectors.
        """
        all_values = set()
        for sig in self.block_sigs.values():
            for vals in sig.concrete_outputs.values():
                all_values.update(vals)
        return tuple(sorted(all_values))

    def get_callee_names(self) -> list[str]:
        """Aggregate unique callee names across all blocks."""
        names = set()
        for sig in self.block_sigs.values():
            names.update(sig.callee_names)
        return sorted(names)

    def get_cfg_shape_features(self) -> dict:
        """Compute CFG structural shape features.

        Returns dict with: edge_count, loop_count, max_depth,
        cyclomatic_complexity.
        """
        edge_count = self.cfg.number_of_edges() if self.cfg else 0
        node_count = self.cfg.number_of_nodes() if self.cfg else 0

        # Detect loops via back-edges
        loop_count = 0
        max_depth = 0
        if self.cfg and self.cfg.nodes:
            try:
                # Count back-edges (loops)
                entry = list(self.cfg.nodes)[0]
                for u, v in nx.dfs_edges(self.cfg, source=entry):
                    if v in nx.ancestors(self.cfg, u) or v == entry:
                        loop_count += 1
            except nx.NetworkXError:
                pass

            # Max depth via longest shortest path from entry
            try:
                entry = list(self.cfg.nodes)[0]
                lengths = nx.single_source_shortest_path_length(
                    self.cfg, entry
                )
                max_depth = max(lengths.values()) if lengths else 0
            except nx.NetworkXError:
                pass

        # Cyclomatic complexity: E - N + 2P (P=1 for single function)
        cyclomatic = edge_count - node_count + 2

        return {
            'edge_count': edge_count,
            'loop_count': loop_count,
            'max_depth': max_depth,
            'cyclomatic_complexity': cyclomatic,
        }

    def get_string_refs(self) -> list[str]:
        """Aggregate unique string references across all blocks."""
        refs = set()
        for sig in self.block_sigs.values():
            refs.update(sig.string_refs)
        return sorted(refs)

    def to_feature_set(self) -> frozenset:
        """Convert to a set of hashable features for Jaccard similarity."""
        features = set()

        # Aggregate block-level features with weights
        for addr, sig in self.block_sigs.items():
            for feat in sig.to_feature_set():
                features.add(feat)

        # Function-level structural features
        features.add(('num_blocks', min(self.num_blocks, 50)))
        features.add(('num_insns_bucket',
                       self.num_instructions // 10 * 10))

        # Memory pattern features
        mem = self.get_memory_pattern_summary()
        features.add(('stack_depth_bucket',
                       mem['max_stack_depth'] // 16 * 16))

        # CFG shape features (bucketed for set-based matching)
        shape = self.get_cfg_shape_features()
        features.add(('shape', 'edges', min(shape['edge_count'], 100)))
        features.add(('shape', 'loops', shape['loop_count']))
        features.add(('shape', 'depth', min(shape['max_depth'], 20)))
        features.add(('shape', 'cyclomatic',
                       min(shape['cyclomatic_complexity'], 50)))

        # Callee name features (already in block-level, also at function level)
        for name in self.get_callee_names():
            features.add(('call', name))

        # String reference features
        for s in self.get_string_refs():
            features.add(('str', s))

        return frozenset(features)

    def to_dense_vector(self, dim: int = 256) -> np.ndarray:
        """Convert to a fixed-length dense vector using feature hashing."""
        vec = np.zeros(dim, dtype=np.float64)

        for feat in self.to_feature_set():
            h = int(hashlib.md5(
                str(feat).encode()
            ).hexdigest(), 16)
            idx = h % dim
            sign = 1 if (h // dim) % 2 == 0 else -1
            vec[idx] += sign

        # L2 normalize
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec /= norm

        return vec
