# syntax=docker/dockerfile:1.6
# RustDiff — final project reproduction image (Intel/x86-64).
#
# Build:  docker build -t rustdiff .
# Run:    docker run --rm \
#             -v "$PWD/experiments/rust_features/results:/app/experiments/rust_features/results" \
#             rustdiff
#
# Default CMD runs the full analysis and writes analysis_data.json
# into the mounted results directory.

# ── Stage 1: build rustfilt ──────────────────────────────────────────────────
# rustfilt is used by rustdiff/rust/demangle.py to resolve Rust symbols.
# We build it in a throw-away Rust image so the final image stays slim.
FROM --platform=linux/amd64 rust:1.82-slim-bookworm AS rustfilt-builder
RUN cargo install rustfilt --locked --root /out

# ── Stage 2: runtime ─────────────────────────────────────────────────────────
FROM --platform=linux/amd64 python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

# System deps:
#   git               — initialize the vSim submodule during image build
#   gcc / build-essential — needed by a couple of Python wheels (pyvex, claripy)
#   libffi / libssl   — runtime deps of pyvex / z3
#   binutils          — objdump etc. (used by angr in a few paths)
RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        build-essential \
        pkg-config \
        libffi-dev \
        libssl-dev \
        binutils \
    && rm -rf /var/lib/apt/lists/*

# Copy the rustfilt binary from stage 1.
COPY --from=rustfilt-builder /out/bin/rustfilt /usr/local/bin/rustfilt

WORKDIR /app

# Install Python deps first for good layer caching.
# We deliberately pin the angr family at 9.2.138 (the version rustdiff was
# written against — see pyproject.toml). requirements.txt in the repo lists
# a newer snapshot that is NOT API-compatible with vSim; we override it.
COPY requirements.txt pyproject.toml ./
RUN pip install \
        "angr==9.2.138" "claripy==9.2.138" "pyvex==9.2.138" \
        "cle==9.2.138"  "archinfo==9.2.138" \
        "pycparser<2.22"  \
        "networkx==3.3" "numpy==2.2.4" "pandas==2.2.3" \
        "scipy==1.15.2" "scikit-learn==1.6.1" "tqdm==4.66.5" \
        "matplotlib==3.10.1" "pyelftools==0.32" "python-pptx==1.0.2"

# Copy the rest of the project.
COPY . .

# If vendor/vSim is empty (submodule not initialized on the host), clone it
# inside the image so the build is self-contained.
RUN if [ ! -d vendor/vSim/src ]; then \
        rm -rf vendor/vSim && \
        git clone --depth 1 https://github.com/OSUSecLab/vSim.git vendor/vSim ; \
    fi

# Install rustdiff itself in editable mode so rustdiff.* imports resolve.
RUN pip install -e . --no-deps

# Smoke test: make sure imports work and rustfilt is callable.
RUN rustfilt --version >/dev/null \
    && python -c "import angr, claripy, networkx, scipy, numpy, pandas, elftools; print('deps ok')" \
    && python -c "import rustdiff; from rustdiff.loader import RustBinaryLoader; print('rustdiff ok')"

# Default: run the main experiment. Mount the results dir to get output out.
CMD ["python", "experiments/rust_features/run_analysis.py"]
