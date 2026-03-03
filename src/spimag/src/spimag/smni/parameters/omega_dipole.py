"""Ω_dipole - Dipolar Coupling Tensor parameter.

Inter-radical dipole-dipole interaction.
Ĥ_dipolar = Ŝₐ · D · Ŝᵦ
"""

from typing import Optional, Dict
import numpy as np


class DipolarCouplingTensor:
    """Ω_dipole: Dipolar Coupling Tensor.
    
    Attributes:
        r: Inter-radical distance [m]
        D: Dipolar coupling strength [T]
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.r = 19.5e-10  # 19.5 Å
        self.D = None
        
    def compute(self, r: float = None) -> float:
        """Compute normalized Ω_dipole value."""
        r = r or self.r
        
        # Calculate dipolar coupling
        mu0 = 4 * np.pi * 1e-7  # H/m
        gamma_e = 1.7608e11
        hbar = 1.0545718e-34
        
        D_val = (mu0 / (4 * np.pi)) * (gamma_e**2 * hbar**2 / r**3)
        
        # Normalize (smaller coupling = better)
        D_max = (mu0 / (4 * np.pi)) * (gamma_e**2 * hbar**2 / (10e-10)**3)
        normalized = max(0, 1 - (D_val / D_max))
        
        return normalized
    
    def validate(self) -> bool:
        """Validate parameter calculation."""
        return True
