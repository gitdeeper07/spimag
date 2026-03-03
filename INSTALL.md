# ⚛️ SPIMAG INSTALLATION GUIDE

This guide covers installation of the SPIMAG framework for quantum biophysical magnetoreception analysis.

---

## Table of Contents
- [System Requirements](#system-requirements)
- [Quick Installation](#quick-installation)
- [Detailed Installation](#detailed-installation)
  - [1. Python Environment](#1-python-environment)
  - [2. Install SPIMAG](#2-install-spimag)
  - [3. Database Setup](#3-database-setup)
  - [4. Configuration](#4-configuration)
  - [5. Verify Installation](#5-verify-installation)
- [Platform-Specific Instructions](#platform-specific-instructions)
  - [Linux / Ubuntu](#linux--ubuntu)
  - [macOS](#macos)
  - [Windows](#windows)
  - [Termux (Android)](#termux-android)
- [Docker Installation](#docker-installation)
- [Development Installation](#development-installation)
- [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum Requirements
- **Python**: 3.8 or higher
- **RAM**: 8 GB (16 GB recommended for spin dynamics simulations)
- **Storage**: 10 GB free space
- **OS**: Linux, macOS, Windows, or Termux (Android)

### Optional Requirements
- **GPU**: CUDA-capable (for ML acceleration and PI-QNN)
- **Database**: PostgreSQL 13+ (for production)
- **Quantum Chemistry Software**: ORCA 5.0+ (for hyperfine tensor calculations)

---

## Quick Installation

```bash
# Install from PyPI
pip install spimag

# Verify installation
spimag --version
spimag doctor  # Check system compatibility
```

---

Detailed Installation

1. Python Environment

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Upgrade pip
pip install --upgrade pip setuptools wheel
```

2. Install SPIMAG

```bash
# Basic installation
pip install spimag

# With all optional dependencies
pip install "spimag[all]"

# Or specific extras
pip install "spimag[ml]"      # For machine learning features (PI-QNN)
pip install "spimag[quantum]"  # For quantum chemistry integration
pip install "spimag[viz]"      # For visualization
pip install "spimag[web]"      # For web dashboard
pip install "spimag[dev]"      # For development
```

3. Database Setup (Optional)

For production deployments storing spin dynamics data:

```bash
# Install PostgreSQL (Ubuntu)
sudo apt install postgresql postgresql-contrib

# Create database
sudo -u postgres createdb spimag
sudo -u postgres createuser --interactive
# Create spimag_user with password

# Initialize schema
psql -U spimag_user -d spimag -f schema.sql
```

4. Configuration

```bash
# Create configuration directory
mkdir -p ~/.spimag
mkdir -p ~/.spimag/data
mkdir -p ~/.spimag/logs
mkdir -p ~/.spimag/results

# Copy default configuration
cp config/spimag.default.yaml ~/.spimag/config.yaml

# Edit configuration
nano ~/.spimag/config.yaml
# Set database credentials, API keys, hyperfine tensor paths

# Set environment variable
export SPIMAG_CONFIG=~/.spimag/config.yaml
# Add to .bashrc or .zshrc for persistence
```

5. Verify Installation

```bash
# Run diagnostics
spimag doctor

# Expected output:
# ✓ Python 3.8+ detected
# ✓ Dependencies installed
# ✓ Configuration file found
# ✓ SMNI module loaded
# ✓ Database connection successful (if configured)

# Run tests
pytest --pyargs spimag -v

# Test with sample data
spimag demo --species erithacus-rubecula

# Check parameter correlations
spimag check-correlation --expected 0.948
```

---

Platform-Specific Instructions

Linux / Ubuntu

```bash
# Install system dependencies
sudo apt update
sudo apt install -y \
    python3.10 python3.10-dev python3.10-venv \
    build-essential libssl-dev libffi-dev \
    libhdf5-dev libnetcdf-dev \
    postgresql postgresql-contrib \
    gfortran  # For quantum chemistry libraries

# Install SPIMAG
pip install spimag[all]
```

macOS

```bash
# Install Homebrew if not present
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and dependencies
brew install python@3.10
brew install hdf5 netcdf
brew install postgresql@14

# Install SPIMAG
pip install spimag[all]
```

Windows

Using WSL2 (Recommended)

```bash
# In PowerShell as Administrator
wsl --install -d Ubuntu

# Then follow Linux instructions inside WSL
```

Native Windows

```bash
# Download Python 3.10 from python.org
# Open PowerShell as Administrator

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install SPIMAG
pip install spimag[all]
```

Termux (Android)

For field data collection and analysis on mobile devices:

```bash
# Update packages
pkg update && pkg upgrade

# Install Python and dependencies
pkg install python python-pip
pkg install libxml2 libxslt
pkg install openblas  # For numerical computing

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install SPIMAG (core only, no ML/quantum)
pip install spimag

# Note: ML and quantum features are limited on mobile devices
# Use for data collection and basic analysis only
```

---

Docker Installation

Using pre-built image

```bash
# Pull image
docker pull gitlab.com/gitdeeper07/spimag:latest

# Run container
docker run -it \
  --name spimag \
  -v ~/.spimag:/root/.spimag \
  -v ~/field_data:/data/field \
  -e SPIMAG_CONFIG=/root/.spimag/config.yaml \
  -p 8501:8501 \
  gitlab.com/gitdeeper07/spimag:latest
```

Docker Compose (full stack)

```yaml
# docker-compose.yml
version: '3.8'

services:
  api:
    image: gitlab.com/gitdeeper07/spimag:latest
    command: spimag serve --api
    ports:
      - "8000:8000"
    volumes:
      - ./config:/root/.spimag
      - ./data:/data
    environment:
      - SPIMAG_CONFIG=/root/.spimag/config.yaml
    depends_on:
      - postgres
      - redis

  dashboard:
    image: gitlab.com/gitdeeper07/spimag:latest
    command: spimag serve --dashboard
    ports:
      - "8501:8501"
    volumes:
      - ./config:/root/.spimag
    environment:
      - SPIMAG_CONFIG=/root/.spimag/config.yaml
      - API_URL=http://api:8000
    depends_on:
      - api

  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: spimag
      POSTGRES_USER: spimag_user
      POSTGRES_PASSWORD: secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./schema.sql:/docker-entrypoint-initdb.d/schema.sql

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - api
      - dashboard

volumes:
  postgres_data:
  redis_data:
```

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

Development Installation

For contributors and developers:

```bash
# Clone repository
git clone https://gitlab.com/gitdeeper07/spimag.git
cd spimag

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install in development mode with all extras
pip install -e ".[all,dev]"

# Install pre-commit hooks
pre-commit install

# Run tests
pytest tests/ -v --cov=spimag

# Run hypothesis tests (H1-H8)
pytest tests/hypothesis/ -v
```

---

Configuration Reference

Main Configuration File

```yaml
# ~/.spimag/config.yaml

# SPIMAG Configuration
version: 1.0

# Project settings
project:
  name: "SPIMAG"
  species: 31
  datasets: 2491
  version: 1.0.0

# Database
database:
  url: postgresql://spimag_user:password@localhost:5432/spimag
  pool_size: 10
  timeout: 30

# SMNI Parameters
parameters:
  S_yield:
    enabled: true
    calibration_file: calibrations/s_yield_2026.json
    phi_rp_threshold: 0.85
  Gamma_coh:
    enabled: true
    coherence_threshold_microsec: 4.7
    measurement_temp_celsius: 37
  Theta_inc:
    enabled: true
    precision_threshold_degrees: 5.0
  Chi_para:
    enabled: true
    magnetite_sensitivity_JpT: 1.4e-17

# AI Ensemble
ai:
  model: ensemble
  cnn_layers: 3
  xgboost_rounds: 100
  lstm_units: 64
  pi_qnn_enabled: true
  batch_size: 32
  epochs: 50

# Dashboard
dashboard:
  host: 0.0.0.0
  port: 8501
  theme: dark
  refresh_rate: 30  # seconds
  storm_monitoring: true

# Field data
field:
  data_dir: /data/field
  backup_dir: /data/backup
  auto_upload: true
  compression: gzip

# External APIs
external:
  noaa:
    enabled: true
    api_key: ${NOAA_API_KEY}
    update_interval: 30
  intermagnet:
    enabled: true
    token: ${INTERMAGNET_TOKEN}
    observatories: 185

# Logging
logging:
  level: INFO
  file: logs/spimag.log
  max_size: 100MB
  backup_count: 5
```

---

Troubleshooting

Common Issues

Package not found

```bash
# Ensure pip is up to date
pip install --upgrade pip

# Try installing with --no-cache-dir
pip install --no-cache-dir spimag

# Check Python version
python --version  # Must be >=3.8
```

Import errors

```bash
# Check Python path
python -c "import sys; print(sys.path)"

# Ensure virtual environment is activated
which python

# Reinstall package
pip uninstall spimag -y
pip install spimag
```

Memory issues with spin dynamics

```bash
# Reduce batch size
export SPIMAG_BATCH_SIZE=100

# Use chunked processing
spimag analyze --chunk-size 1000

# For large datasets, use:
spimag analyze --memory-efficient
```

Quantum chemistry integration issues

```bash
# Check ORCA installation
spimag doctor --quantum

# Test hyperfine tensor calculation
python scripts/test_hyperfine.py --molecule fad

# Use built-in tensor library
spimag config set use_builtin_tensors true
```

Database connection

```bash
# Test connection
spimag db test

# Initialize database
spimag db init --force

# Backup database
spimag db backup --output backup.sql
```

NOAA/INTERMAGNET API issues

```bash
# Test API connections
spimag api test --service noaa
spimag api test --service intermagnet

# Update API keys
spimag config set noaa_api_key YOUR_KEY
spimag config set intermagnet_token YOUR_TOKEN
```

---

Getting Help

· Documentation: https://spimag.readthedocs.io
· Dashboard: https://spimag.netlify.app
· Issues: https://gitlab.com/gitdeeper07/spimag/-/issues
· Discussions: https://gitlab.com/gitdeeper07/spimag/-/discussions
· Email: support@spimag.org
· Principal Investigator: gitdeeper@gmail.com

---

Verification Script

```python
# verify.py
import spimag
print(f"SPIMAG version: {spimag.__version__}")
print(f"SMNI accuracy: {spimag.SMNI_ACCURACY}%")
print(f"Parameters: {spimag.PARAMETERS}")
print(f"Species: {spimag.SPECIES_COUNT}")
print("Installation successful! ⚛️")
```

---

Live Dashboard: https://spimag.netlify.app
Documentation: https://spimag.readthedocs.io
DOI: 10.14293/SPIMAG.2026.001

⚛️ Inside the eye of a migrating robin, two electrons are entangled. SPIMAG decodes.
