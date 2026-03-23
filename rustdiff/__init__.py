"""RustDiff: Value-based function fingerprinting for Rust binary diffing."""

import os
import sys

# Make vSim importable: add vendor/vSim/ to sys.path so that vSim's
# internal `from src.xxx import ...` resolves to vendor/vSim/src/xxx.
_vsim_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'vendor', 'vSim')
)
if _vsim_root not in sys.path:
    sys.path.insert(0, _vsim_root)
