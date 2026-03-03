#!/usr/bin/env python3
"""⚛️ SPIMAG: Spin-Induced Magnetic Alignment & Geospatial Intelligence.

A quantum biophysical framework for decoding cryptochrome-based magnetoreception
in migratory animals and its applications to geospatial navigation intelligence.

Dashboard: https://spimag.netlify.app
API: https://spimag.netlify.app/api
Documentation: https://spimag.readthedocs.io
DOI: 10.14293/SPIMAG.2026.001
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="spimag",
    version="1.0.0",
    author="Samir Baladi",
    author_email="gitdeeper@gmail.com",
    description="SPIMAG: Spin-Induced Magnetic Alignment & Geospatial Intelligence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/gitdeeper07/spimag",
    project_urls={
        "Bug Tracker": "https://gitlab.com/gitdeeper07/spimag/-/issues",
        "Documentation": "https://spimag.readthedocs.io",
        "Dashboard": "https://spimag.netlify.app",
        "API": "https://spimag.netlify.app/api",
        "DOI": "https://doi.org/10.14293/SPIMAG.2026.001",
        "Source Code": "https://gitlab.com/gitdeeper07/spimag",
        "GitHub": "https://github.com/gitdeeper07/spimag",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "ml": [
            "tensorflow>=2.8.0",
            "torch>=1.10.0",
            "pytorch-lightning>=1.6.0",
        ],
        "quantum": [
            "pyscf>=2.0.0",
            "openfermion>=1.0.0",
            "cirq>=0.13.0",
        ],
        "viz": [
            "streamlit>=1.15.0",
            "plotly>=5.5.0",
            "dash>=2.0.0",
            "folium>=0.14.0",
        ],
        "web": [
            "flask>=2.0.0",
            "flask-cors>=3.0.0",
            "flask-restful>=0.3.9",
            "fastapi>=0.85.0",
            "uvicorn>=0.18.0",
            "gunicorn>=20.1.0",
        ],
        "geo": [
            "geopandas>=0.10.0",
            "shapely>=1.8.0",
            "rasterio>=1.3.0",
            "pyproj>=3.3.0",
        ],
        "field": [
            "pyserial>=3.5",
            "pymodbus>=3.0.0",
            "minimalmodbus>=2.0.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "ruff>=0.0.260",
            "mypy>=0.990",
            "pre-commit>=2.20.0",
            "mkdocs>=1.4.0",
            "mkdocs-material>=9.0.0",
            "mkdocstrings>=0.20.0",
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
        "all": [
            "tensorflow>=2.8.0",
            "torch>=1.10.0",
            "pytorch-lightning>=1.6.0",
            "pyscf>=2.0.0",
            "openfermion>=1.0.0",
            "cirq>=0.13.0",
            "streamlit>=1.15.0",
            "plotly>=5.5.0",
            "dash>=2.0.0",
            "folium>=0.14.0",
            "flask>=2.0.0",
            "flask-cors>=3.0.0",
            "flask-restful>=0.3.9",
            "fastapi>=0.85.0",
            "uvicorn>=0.18.0",
            "gunicorn>=20.1.0",
            "geopandas>=0.10.0",
            "shapely>=1.8.0",
            "rasterio>=1.3.0",
            "pyproj>=3.3.0",
            "pyserial>=3.5",
            "pymodbus>=3.0.0",
            "minimalmodbus>=2.0.0",
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "ruff>=0.0.260",
            "mypy>=0.990",
            "pre-commit>=2.20.0",
            "mkdocs>=1.4.0",
            "mkdocs-material>=9.0.0",
            "mkdocstrings>=0.20.0",
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "spimag = spimag.cli.main:cli",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "quantum-biology",
        "cryptochrome",
        "magnetoreception",
        "radical-pair-mechanism",
        "spin-dynamics",
        "zeeman-effect",
        "avian-navigation",
        "bio-inspired-sensors",
        "geomagnetic-storms",
    ],
)

# ⚛️ Inside the eye of a migrating robin, two electrons are entangled. SPIMAG decodes.
