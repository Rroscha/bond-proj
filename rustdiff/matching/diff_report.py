"""Diff report generation for supply chain attack detection."""

import json
from pathlib import Path

from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint


class DiffReport:
    """Generate a report comparing two binaries.

    Categorizes functions as: matched, modified, new, or removed.
    Provides block-level drill-down for modified functions.
    """

    def __init__(self, flagged: dict,
                 fps1: dict[int, FunctionFingerprint],
                 fps2: dict[int, FunctionFingerprint],
                 bin1_path: str, bin2_path: str):
        self.flagged = flagged
        self.fps1 = fps1
        self.fps2 = fps2
        self.bin1_path = bin1_path
        self.bin2_path = bin2_path

    def generate_summary(self) -> dict:
        """High-level summary of the diff."""
        return {
            'binary1': self.bin1_path,
            'binary2': self.bin2_path,
            'total_functions_bin1': len(self.fps1),
            'total_functions_bin2': len(self.fps2),
            'matched': len(self.flagged['matched']),
            'modified': len(self.flagged['modified']),
            'new': len(self.flagged['new']),
            'removed': len(self.flagged['removed']),
        }

    def generate_detailed_report(self) -> dict:
        """Full report with per-function details."""
        report = self.generate_summary()

        report['modified_functions'] = []
        for entry in self.flagged['modified']:
            detail = dict(entry)
            # Add block-level comparison for modified functions
            fp1 = self.fps1.get(entry['addr1'])
            fp2 = self.fps2.get(entry['addr2'])
            if fp1 and fp2:
                detail['blocks_bin1'] = fp1.num_blocks
                detail['blocks_bin2'] = fp2.num_blocks
                detail['insns_bin1'] = fp1.num_instructions
                detail['insns_bin2'] = fp2.num_instructions
            report['modified_functions'].append(detail)

        report['new_functions'] = self.flagged['new']
        report['removed_functions'] = self.flagged['removed']

        # Top matched by similarity (sample)
        report['top_matches'] = self.flagged['matched'][:20]

        return report

    def to_json(self, path: str):
        """Write report as JSON."""
        report = self.generate_detailed_report()
        Path(path).write_text(json.dumps(report, indent=2, default=str))

    def format_text_summary(self) -> str:
        """Format a human-readable text summary."""
        s = self.generate_summary()
        lines = [
            f"Binary Diff Report",
            f"  Binary 1: {s['binary1']}",
            f"  Binary 2: {s['binary2']}",
            f"",
            f"  Functions in Binary 1: {s['total_functions_bin1']}",
            f"  Functions in Binary 2: {s['total_functions_bin2']}",
            f"",
            f"  Matched (unchanged): {s['matched']}",
            f"  Modified:            {s['modified']}",
            f"  New (in Binary 2):   {s['new']}",
            f"  Removed:             {s['removed']}",
        ]

        if self.flagged['modified']:
            lines.append("")
            lines.append("Modified Functions:")
            for entry in self.flagged['modified']:
                lines.append(
                    f"  {entry['name1']} <-> {entry['name2']}  "
                    f"(sim={entry['similarity']:.3f})"
                )

        if self.flagged['new']:
            lines.append("")
            lines.append("New Functions:")
            for entry in self.flagged['new']:
                lines.append(f"  {entry['name']}")

        if self.flagged['removed']:
            lines.append("")
            lines.append("Removed Functions:")
            for entry in self.flagged['removed']:
                lines.append(f"  {entry['name']}")

        return '\n'.join(lines)
