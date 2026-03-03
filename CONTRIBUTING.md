# ⚛️ CONTRIBUTING TO SPIMAG

First off, thank you for considering contributing to SPIMAG! We welcome contributions from quantum physicists, biophysicists, ornithologists, behavioral ecologists, data scientists, software engineers, and anyone passionate about understanding quantum phenomena in biological systems.

---

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

## Types of Contributions

### 🧪 Scientific Contributions
- New cryptochrome spin dynamics data
- Behavioral orientation experiments in migratory species
- RF field disruption studies
- Quantum chemistry calculations (DFT, hyperfine tensors)
- Structural biology data (crystallography, Cryo-EM)

### 💻 Code Contributions
- SMNI calculation engine improvements
- PI-QNN (Physics-Informed Quantum Neural Network) enhancements
- Spin dynamics solvers (Stochastic Liouville Equation)
- Hyperfine tensor parameterization
- Dashboard and visualization tools

### 📊 Data Contributions
- Transient absorption spectroscopy measurements
- Electron paramagnetic resonance (EPR) data
- Emlen funnel orientation datasets
- Geomagnetic field recordings
- RF field surveys
- Species migration tracking data

### 📝 Documentation Contributions
- Tutorials and examples
- API documentation
- Parameter explanations
- Case study write-ups
- Translation of documentation

---

## Getting Started

### Prerequisites
- **Python 3.8–3.11**
- **Git**
- **Basic knowledge of quantum mechanics or biophysics**

### Setup Development Environment

```bash
# Fork the repository, then clone
git clone https://gitlab.com/YOUR_USERNAME/spimag.git
cd spimag

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install development dependencies
pip install -e ".[dev]"
pre-commit install
```

Verify Setup

```bash
# Run basic validation
python scripts/validate_environment.py

# Run tests
pytest tests/unit/ -v

# Check parameter correlations
python scripts/check_correlation.py --expected 0.948
```

---

Development Workflow

1. Create an issue describing your proposed changes
2. Fork and branch:
   ```bash
   git checkout -b feature/your-feature-name
   git checkout -b fix/issue-description
   git checkout -b species/new-species-name
   ```
3. Make changes following our standards
4. Write/update tests
5. Run tests locally
6. Commit with clear messages
7. Push to your fork
8. Open a Merge Request

---

Coding Standards

Python

· Format: Black (line length 88)
· Imports: isort with black profile
· Type Hints: Required for all public functions
· Docstrings: Google style

Example Parameter Module

```python
"""S_yield - Spin Quantum Yield parameter."""

from typing import Optional
import numpy as np

from spimag.core import ParameterBase


class SpinQuantumYield(ParameterBase):
    """S_yield: Spin Quantum Yield.
    
    Measures photon-to-radical-pair conversion efficiency.
    
    Attributes:
        phi_rp: Measured quantum yield (0-1)
        k_et: Forward electron transfer rate [s⁻¹]
        k_rec: Geminate recombination rate [s⁻¹]
    """
    
    def compute(self) -> float:
        """Compute normalized S_yield value."""
        # Implementation
        pass
```

---

Testing Guidelines

Test Structure

```
tests/
├── unit/                    # Unit tests
│   ├── parameters/
│   │   ├── test_s_yield.py
│   │   └── test_gamma_coh.py
├── integration/             # Integration tests
├── hypothesis/              # Hypothesis validation (H1-H8)
└── fixtures/                # Test data
```

Running Tests

```bash
# All tests
pytest

# Hypothesis tests (H1-H8)
pytest tests/hypothesis/ -v

# With coverage
pytest --cov=spimag --cov-report=html
```

---

Data Contributions

New Species Data

When adding data for a new migratory species, include:

1. Species metadata (taxonomy, migration route, habitat)
2. Cryptochrome sequence or structure data
3. Behavioral orientation data (Emlen funnel trials)
4. Spin dynamics measurements (if available)
5. RF sensitivity data (if available)

Data Format Requirements

Parameter Format Min Samples
S_yield .csv with excitation wavelengths 3 replicates
Γ_coh .csv with decay curves 10 measurements
θ_inc .csv with angular distributions 30 trials
P_singlet .csv with field dependence 5 field strengths

---

Animal Research Ethics

Any contribution involving animal research must:

1. Obtain ethics approval - Document from institutional animal care committee
2. Follow guidelines - Adhere to local and international animal welfare standards
3. Minimize stress - Use non-invasive methods where possible
4. Proper housing - Ensure appropriate conditions for captive animals
5. Release protocols - Follow proper release procedures for wild-caught animals

Contact: ethics@spimag.org

---

Adding New Parameters

If you propose a new parameter for SMNI:

1. Literature review - Demonstrate scientific basis
2. Physical independence - Show minimal correlation with existing parameters
3. Measurement protocol - Define how to measure it
4. Validation data - Provide dataset showing predictive power
5. Weight proposal - Suggest initial weight (<5% typically)

---

Reporting Issues

Bug Reports

Include:

· Clear title and description
· Steps to reproduce
· Expected vs actual behavior
· Environment details
· Logs or screenshots

Feature Requests

Include:

· Use case description
· Expected behavior
· Scientific justification
· References to similar work

---

Contact

Purpose Contact
General inquiries gitdeeper@gmail.com
Code of Conduct conduct@spimag.org
Animal ethics ethics@spimag.org
Data contributions data@spimag.org

Repository: https://gitlab.com/gitdeeper07/spimag
Dashboard: https://spimag.netlify.app
DOI: 10.14293/SPIMAG.2026.001

---

⚛️ Inside the eye of a migrating robin, two electrons are entangled. SPIMAG decodes.

Last Updated: March 2026
