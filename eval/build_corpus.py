"""Build a corpus of Rust binaries under varying compilation conditions."""

import logging
import os
import subprocess
import shutil
from itertools import product
from pathlib import Path

logger = logging.getLogger(__name__)

# Small, focused crates for initial development
DEFAULT_CRATES = [
    'tiny-keccak',   # Pure computation (hashing)
    'base64',        # Simple transformations
    'crc32fast',     # Checksum computation
]

DEFAULT_OPT_LEVELS = ['0', '1', '2', '3']

DEFAULT_CONFIGS = [
    {'opt_level': opt}
    for opt in DEFAULT_OPT_LEVELS
]


class RustCorpusBuilder:
    """Build Rust crates under varying compilation conditions.

    Dimensions of variation:
    - Optimization level: -C opt-level=0,1,2,3,s,z
    - Rustc version: stable, specific versions
    - LTO: thin, fat, off
    - Strip: none, debuginfo, symbols
    """

    def __init__(self, corpus_dir: str):
        self.corpus_dir = Path(corpus_dir)
        self.corpus_dir.mkdir(parents=True, exist_ok=True)
        self._verify_toolchain()

    def _verify_toolchain(self):
        """Check that cargo and rustc are available."""
        for tool in ('cargo', 'rustc'):
            if not shutil.which(tool):
                raise RuntimeError(f'{tool} not found in PATH')
        result = subprocess.run(
            ['rustc', '--version'],
            capture_output=True, text=True,
        )
        logger.info('Using %s', result.stdout.strip())

    def build_binary(
        self,
        crate_name: str,
        crate_version: str | None = None,
        opt_level: str = '2',
        lto: str = 'off',
        strip: str = 'none',
        extra_rustflags: str = '',
    ) -> Path | None:
        """Build a single binary configuration.

        Returns path to the built binary, or None on failure.
        """
        # Create a temporary cargo project that depends on the crate
        config_tag = f'O{opt_level}_lto-{lto}_strip-{strip}'
        build_dir = self.corpus_dir / crate_name / config_tag
        build_dir.mkdir(parents=True, exist_ok=True)

        # Build RUSTFLAGS
        rustflags = f'-C opt-level={opt_level}'
        if lto != 'off':
            rustflags += f' -C lto={lto}'
        if strip == 'symbols':
            rustflags += ' -C strip=symbols'
        elif strip == 'debuginfo':
            rustflags += ' -C strip=debuginfo'
        if extra_rustflags:
            rustflags += f' {extra_rustflags}'

        # Create Cargo.toml
        version_spec = f'"{crate_version}"' if crate_version else '"*"'
        cargo_toml = build_dir / 'Cargo.toml'
        cargo_toml.write_text(f"""[package]
name = "{crate_name}-bench"
version = "0.1.0"
edition = "2021"

[[bin]]
name = "bench"
path = "src/main.rs"

[dependencies]
{crate_name} = {version_spec}

[profile.release]
opt-level = {opt_level}
debug = true
""")

        # Create minimal main.rs that exercises the crate
        src_dir = build_dir / 'src'
        src_dir.mkdir(exist_ok=True)
        main_rs = src_dir / 'main.rs'
        main_rs.write_text(self._generate_main_rs(crate_name))

        # Run cargo build
        env = os.environ.copy()
        env['RUSTFLAGS'] = rustflags

        logger.info('Building %s [%s]', crate_name, config_tag)
        try:
            result = subprocess.run(
                ['cargo', 'build', '--release'],
                cwd=str(build_dir),
                env=env,
                capture_output=True,
                text=True,
                timeout=300,
            )
            if result.returncode != 0:
                logger.error('Build failed for %s [%s]: %s',
                             crate_name, config_tag, result.stderr)
                return None
        except subprocess.TimeoutExpired:
            logger.error('Build timed out for %s [%s]', crate_name, config_tag)
            return None

        # Find the built binary
        bin_path = build_dir / 'target' / 'release' / 'bench'
        if not bin_path.exists():
            logger.error('Binary not found at %s', bin_path)
            return None

        # Copy to a more accessible location
        output_path = self.corpus_dir / crate_name / f'bench_{config_tag}'
        shutil.copy2(bin_path, output_path)
        logger.info('Built: %s', output_path)
        return output_path

    def build_all_configs(
        self, crate_name: str,
        opt_levels: list[str] | None = None,
        crate_version: str | None = None,
    ) -> list[Path]:
        """Build a crate under all specified optimization levels."""
        if opt_levels is None:
            opt_levels = DEFAULT_OPT_LEVELS

        results = []
        for opt in opt_levels:
            path = self.build_binary(
                crate_name,
                crate_version=crate_version,
                opt_level=opt,
            )
            if path:
                results.append(path)
        return results

    def generate_binary_pairs(
        self, binary_paths: list[Path]
    ) -> list[tuple[Path, Path]]:
        """Generate all pairs for pairwise comparison.

        Returns list of (bin_a, bin_b) tuples.
        """
        pairs = []
        for i, a in enumerate(binary_paths):
            for b in binary_paths[i + 1:]:
                pairs.append((a, b))
        return pairs

    @staticmethod
    def _generate_main_rs(crate_name: str) -> str:
        """Generate a minimal main.rs that uses the target crate."""
        # Simple stubs that exercise basic crate functionality
        if crate_name == 'tiny-keccak':
            return """
use tiny_keccak::{Hasher, Sha3};
fn main() {
    let mut sha3 = Sha3::v256();
    sha3.update(b"hello world");
    let mut output = [0u8; 32];
    sha3.finalize(&mut output);
    println!("{:?}", output);
}
"""
        elif crate_name == 'base64':
            return """
use base64::{Engine as _, engine::general_purpose};
fn main() {
    let encoded = general_purpose::STANDARD.encode(b"hello world");
    println!("{}", encoded);
    let decoded = general_purpose::STANDARD.decode(&encoded).unwrap();
    println!("{:?}", decoded);
}
"""
        elif crate_name == 'crc32fast':
            return """
fn main() {
    let mut hasher = crc32fast::Hasher::new();
    hasher.update(b"hello world");
    let checksum = hasher.finalize();
    println!("{}", checksum);
}
"""
        else:
            return f"""
// Generic stub for {crate_name}
fn main() {{
    println!("stub for {crate_name}");
}}
"""
