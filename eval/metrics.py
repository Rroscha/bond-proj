"""Evaluation metrics for function matching."""

import numpy as np


class MatchingMetrics:
    """Compute evaluation metrics for function matching results."""

    @staticmethod
    def top_k_accuracy(
        matches: list[tuple[int, int, float]],
        sim_matrix: np.ndarray,
        addrs1: list[int],
        addrs2: list[int],
        gt_pairs: list[tuple[int, int]],
        k_list: list[int] = None,
    ) -> dict[int, float]:
        """Compute top-K accuracy.

        For each groundtruth pair (a1, a2), check if a2 is in the top-K
        most similar functions to a1.
        """
        if k_list is None:
            k_list = [1, 3, 5, 10]

        addr1_to_idx = {a: i for i, a in enumerate(addrs1)}
        addr2_to_idx = {a: i for i, a in enumerate(addrs2)}

        results = {k: 0 for k in k_list}
        valid_pairs = 0

        for a1, a2 in gt_pairs:
            if a1 not in addr1_to_idx or a2 not in addr2_to_idx:
                continue
            valid_pairs += 1
            i = addr1_to_idx[a1]
            j = addr2_to_idx[a2]

            # Get similarity row for a1, sort by descending similarity
            row = sim_matrix[i]
            ranked_indices = np.argsort(-row)

            # Find rank of the true match
            rank = np.where(ranked_indices == j)[0]
            if len(rank) == 0:
                continue
            rank = rank[0] + 1  # 1-indexed

            for k in k_list:
                if rank <= k:
                    results[k] += 1

        if valid_pairs == 0:
            return {k: 0.0 for k in k_list}

        return {k: count / valid_pairs for k, count in results.items()}

    @staticmethod
    def mrr(
        sim_matrix: np.ndarray,
        addrs1: list[int],
        addrs2: list[int],
        gt_pairs: list[tuple[int, int]],
    ) -> float:
        """Mean Reciprocal Rank."""
        addr1_to_idx = {a: i for i, a in enumerate(addrs1)}
        addr2_to_idx = {a: i for i, a in enumerate(addrs2)}

        reciprocal_ranks = []
        for a1, a2 in gt_pairs:
            if a1 not in addr1_to_idx or a2 not in addr2_to_idx:
                continue
            i = addr1_to_idx[a1]
            j = addr2_to_idx[a2]

            row = sim_matrix[i]
            ranked_indices = np.argsort(-row)
            rank = np.where(ranked_indices == j)[0]
            if len(rank) > 0:
                reciprocal_ranks.append(1.0 / (rank[0] + 1))

        if not reciprocal_ranks:
            return 0.0
        return float(np.mean(reciprocal_ranks))

    @staticmethod
    def recall_at_k(
        sim_matrix: np.ndarray,
        addrs1: list[int],
        addrs2: list[int],
        gt_pairs: list[tuple[int, int]],
        k: int,
    ) -> float:
        """Recall@K: fraction of groundtruth pairs found in top-K."""
        addr1_to_idx = {a: i for i, a in enumerate(addrs1)}
        addr2_to_idx = {a: i for i, a in enumerate(addrs2)}

        found = 0
        total = 0
        for a1, a2 in gt_pairs:
            if a1 not in addr1_to_idx or a2 not in addr2_to_idx:
                continue
            total += 1
            i = addr1_to_idx[a1]
            j = addr2_to_idx[a2]

            row = sim_matrix[i]
            top_k_indices = np.argsort(-row)[:k]
            if j in top_k_indices:
                found += 1

        if total == 0:
            return 0.0
        return found / total

    @staticmethod
    def matching_precision(
        matches: list[tuple[int, int, float]],
        gt_pairs: list[tuple[int, int]],
    ) -> float:
        """Fraction of predicted matches that are correct."""
        gt_set = set(gt_pairs)
        if not matches:
            return 0.0
        correct = sum(1 for a1, a2, _ in matches if (a1, a2) in gt_set)
        return correct / len(matches)
