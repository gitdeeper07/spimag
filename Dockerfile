# ⚛️ SPIMAG Dockerfile
# Spin-Induced Magnetic Alignment & Geospatial Intelligence

FROM python:3.10-slim AS builder

LABEL maintainer="Samir Baladi <gitdeeper@gmail.com>"
LABEL version="1.0.0"
LABEL description="SPIMAG - Quantum Biophysical Framework for Magnetoreception"
LABEL org.opencontainers.image.source="https://gitlab.com/gitdeeper07/spimag"
LABEL org.opencontainers.image.licenses="MIT"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    SPIMAG_HOME=/opt/spimag \
    SPIMAG_CONFIG=/etc/spimag/config.yaml \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    libhdf5-dev \
    libnetcdf-dev \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 -s /bin/bash spimag && \
    mkdir -p /opt/spimag && \
    mkdir -p /etc/spimag && \
    mkdir -p /data/spin && \
    mkdir -p /data/behavioral && \
    mkdir -p /data/geomagnetic && \
    mkdir -p /data/results && \
    chown -R spimag:spimag /opt/spimag /etc/spimag /data

# Switch to builder stage for dependencies
FROM builder AS builder-stage

USER spimag
WORKDIR /opt/spimag

# Copy requirements first for better caching
COPY --chown=spimag:spimag requirements.txt .
COPY --chown=spimag:spimag setup.py .
COPY --chown=spimag:spimag setup.cfg .
COPY --chown=spimag:spimag pyproject.toml .
COPY --chown=spimag:spimag MANIFEST.in .
COPY --chown=spimag:spimag README.md .
COPY --chown=spimag:spimag LICENSE .

# Create src directory structure
RUN mkdir -p src/spimag

# Install dependencies
RUN pip install --user --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.10-slim

# Copy from builder
COPY --from=builder-stage /home/spimag/.local /home/spimag/.local
COPY --from=builder-stage /opt/spimag /opt/spimag

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    libopenblas-base \
    libhdf5-103-1 \
    libnetcdf19 \
    && rm -rf /var/lib/apt/lists/*

# Create spimag user
RUN useradd -m -u 1000 -s /bin/bash spimag && \
    mkdir -p /opt/spimag && \
    mkdir -p /etc/spimag && \
    mkdir -p /data/spin && \
    mkdir -p /data/behavioral && \
    mkdir -p /data/geomagnetic && \
    mkdir -p /data/results && \
    chown -R spimag:spimag /opt/spimag /etc/spimag /data

# Set environment
ENV PATH=/home/spimag/.local/bin:$PATH \
    PYTHONPATH=/opt/spimag:$PYTHONPATH \
    SPIMAG_HOME=/opt/spimag \
    SPIMAG_CONFIG=/etc/spimag/config.yaml

# Copy package files
COPY --chown=spimag:spimag . /opt/spimag

# Install SPIMAG
RUN pip install --user -e /opt/spimag

# Create default config
RUN cp /opt/spimag/config/spimag.default.yaml /etc/spimag/config.yaml 2>/dev/null || echo ""

USER spimag
WORKDIR /opt/spimag

# Expose ports
EXPOSE 8000 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import spimag; print('SPIMAG healthy')" || exit 1

# Default command
CMD ["spimag", "serve", "--all", "--host", "0.0.0.0"]

# ⚛️ Inside the eye of a migrating robin, two electrons are entangled.
