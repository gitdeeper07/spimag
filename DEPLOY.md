# ⚛️ SPIMAG DEPLOYMENT GUIDE

This guide covers deployment options for the SPIMAG framework, including the live dashboard, API services, documentation, and data repositories.

---

## Quick Deployments

### Netlify (Dashboard)

The SPIMAG interactive dashboard is pre-configured for Netlify deployment.

#### Automatic Deployment

1. Connect your Git repository to Netlify
2. Use these settings:
   - Build command: `cd dashboard && npm run build` (if using Node) or leave empty
   - Publish directory: `dashboard/dist` or `dashboard`
   - Environment variables: none required

3. Or use the `netlify.toml` configuration:

```toml
[build]
  publish = "dashboard"

[build.environment]
  PYTHON_VERSION = "3.11"

[[redirects]]
  from = "/api/*"
  to = "https://spimag.netlify.app/api/:splat"
  status = 200
  force = true

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
```

Manual Deployment

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
netlify deploy --prod --dir=dashboard
```

Live dashboard: https://spimag.netlify.app
API endpoint: https://spimag.netlify.app/api

---

ReadTheDocs (Documentation)

Deploy technical documentation to ReadTheDocs.

Configuration

1. Connect your Git repository to readthedocs.org
2. Use the .readthedocs.yaml configuration in this repository
3. Build documentation automatically on push

Documentation: https://spimag.readthedocs.io

---

PyPI (Python Package)

Deploy the core SPIMAG package to PyPI.

Preparation

```bash
# Install build tools
pip install build twine

# Update version in setup.py/pyproject.toml
# Version: 1.0.0

# Create distribution files
python -m build
```

Upload to PyPI

```bash
# Upload to production PyPI
twine upload dist/*

# Install
pip install spimag
```

PyPI package: https://pypi.org/project/spimag

---

Docker Deployment

Build Image

```dockerfile
# Dockerfile
FROM python:3.10-slim

LABEL maintainer="gitdeeper@gmail.com"
LABEL version="1.0.0"
LABEL description="SPIMAG - Spin-Induced Magnetic Alignment Framework"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    SPIMAG_HOME=/opt/spimag \
    SPIMAG_CONFIG=/etc/spimag/config.yaml

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 -s /bin/bash spimag && \
    mkdir -p /opt/spimag && \
    mkdir -p /etc/spimag && \
    mkdir -p /data/field && \
    mkdir -p /data/results && \
    chown -R spimag:spimag /opt/spimag /etc/spimag /data

USER spimag
WORKDIR /opt/spimag

COPY --chown=spimag:spimag requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

COPY --chown=spimag:spimag . .

RUN pip install --user -e .

EXPOSE 8000 8501

CMD ["spimag", "serve", "--all"]
```

Build and Run

```bash
# Build image
docker build -t spimag:1.0.0 .

# Run container
docker run -d \
  --name spimag-prod \
  -p 8000:8000 \
  -p 8501:8501 \
  -v /host/data:/data \
  -v /host/config:/etc/spimag \
  -e SPIMAG_CONFIG=/etc/spimag/config.yaml \
  --restart unless-stopped \
  spimag:1.0.0
```

---

Docker Compose (Full Stack)

```yaml
# docker-compose.yml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    container_name: spimag-postgres
    environment:
      POSTGRES_DB: spimag
      POSTGRES_USER: spimag_user
      POSTGRES_PASSWORD: ${DB_PASSWORD:-change_me}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-db.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    networks:
      - spimag-network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U spimag_user"]
      interval: 10s
      timeout: 5s
      retries: 5

  api:
    build: .
    container_name: spimag-api
    command: spimag serve --api --host 0.0.0.0 --port 8000
    environment:
      SPIMAG_CONFIG: /etc/spimag/config.yaml
      DB_HOST: postgres
      DB_PORT: 5432
      DB_NAME: spimag
      DB_USER: spimag_user
      DB_PASSWORD: ${DB_PASSWORD}
      API_URL: https://spimag.netlify.app/api
      NOAA_API_KEY: ${NOAA_API_KEY}
      INTERMAGNET_TOKEN: ${INTERMAGNET_TOKEN}
    volumes:
      - ./config:/etc/spimag
      - ./data:/data
    ports:
      - "8000:8000"
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - spimag-network
    restart: unless-stopped

  dashboard:
    build: .
    container_name: spimag-dashboard
    command: spimag serve --dashboard --host 0.0.0.0 --port 8501
    environment:
      SPIMAG_CONFIG: /etc/spimag/config.yaml
      API_URL: http://api:8000
      PUBLIC_API_URL: https://spimag.netlify.app/api
    volumes:
      - ./config:/etc/spimag
    ports:
      - "8501:8501"
    depends_on:
      - api
    networks:
      - spimag-network
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    container_name: spimag-nginx
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
      - ./www:/var/www/html
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - api
      - dashboard
    networks:
      - spimag-network
    restart: unless-stopped

networks:
  spimag-network:
    driver: bridge

volumes:
  postgres_data:
```

Deploy with Docker Compose

```bash
# Set environment variables
export DB_PASSWORD=$(openssl rand -base64 32)
export NOAA_API_KEY=your_key_here
export INTERMAGNET_TOKEN=your_token_here

# Create directories
mkdir -p config data backups ssl www

# Copy configuration
cp config/spimag.prod.yaml config/config.yaml

# Start services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

Configuration

Production Configuration

```yaml
# config/spimag.prod.yaml
# SPIMAG Production Configuration

version: 1.0
environment: production

server:
  host: 0.0.0.0
  port: 8000
  workers: 4
  timeout: 120

database:
  host: postgres
  port: 5432
  name: spimag
  user: spimag_user
  password: ${DB_PASSWORD}
  pool_size: 20

monitoring:
  metrics_enabled: true
  metrics_port: 9090
  storm_update_interval: 30  # seconds

security:
  jwt_secret: ${JWT_SECRET}
  jwt_expiry_hours: 24
  rate_limit: 100/minute
  cors_origins:
    - https://spimag.netlify.app
    - https://spimag.readthedocs.io

api:
  public_url: https://spimag.netlify.app/api
  docs_url: https://spimag.readthedocs.io/api

external_apis:
  noaa:
    url: https://services.swpc.noaa.gov
    api_key: ${NOAA_API_KEY}
    endpoints:
      kp_index: /products/noaa-planetary-k-index.json
      goes_magnetometer: /json/goes/magnetometer.json
  intermagnet:
    url: https://imag-data.bgs.ac.uk
    token: ${INTERMAGNET_TOKEN}
    observatories: 185

field_data:
  upload_dir: /data/uploads
  max_file_size: 1GB
  allowed_formats:
    - .csv
    - .npy
    - .json
    - .h5
```

---

Monitoring

Prometheus Configuration

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'spimag'
    static_configs:
      - targets: ['api:8000', 'dashboard:8501']
    metrics_path: /metrics
    scrape_interval: 15s
```

Grafana Dashboard

Import the SPIMAG dashboard template to visualize:

· SMNI scores across species
· Spin coherence lifetimes in real-time
· Geomagnetic storm impact maps
· RF disruption zones
· Parameter correlations
· System health metrics

---

Backup & Recovery

Automated Backup Script

```bash
#!/bin/bash
# backup.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups"

# Database backup
pg_dump -h postgres -U spimag_user spimag | gzip > $BACKUP_DIR/db_$DATE.sql.gz

# Spin dynamics data backup
tar -czf $BACKUP_DIR/spin_data_$DATE.tar.gz /data/spin

# Configuration backup
tar -czf $BACKUP_DIR/config_$DATE.tar.gz /etc/spimag

# Clean old backups (keep 30 days)
find $BACKUP_DIR -type f -mtime +30 -delete

echo "Backup completed: $DATE"
```

---

Quick Reference

```bash
# Netlify Dashboard
https://spimag.netlify.app
https://spimag.netlify.app/api

# PyPI Package
pip install spimag

# Docker
docker pull gitlab.com/gitdeeper07/spimag:latest

# Documentation
https://spimag.readthedocs.io

# Source Code
https://gitlab.com/gitdeeper07/spimag
https://github.com/gitdeeper07/spimag

# NOAA Space Weather
https://swpc.noaa.gov

# INTERMAGNET
https://intermagnet.org
```

---

Support

For deployment assistance:

· Dashboard: https://spimag.netlify.app
· Documentation: https://spimag.readthedocs.io
· Issues: https://gitlab.com/gitdeeper07/spimag/-/issues
· Email: deploy@spimag.org
· Principal Investigator: gitdeeper@gmail.com

---

⚛️ Inside the eye of a migrating robin, two electrons are entangled. SPIMAG decodes.

DOI: 10.14293/SPIMAG.2026.001
