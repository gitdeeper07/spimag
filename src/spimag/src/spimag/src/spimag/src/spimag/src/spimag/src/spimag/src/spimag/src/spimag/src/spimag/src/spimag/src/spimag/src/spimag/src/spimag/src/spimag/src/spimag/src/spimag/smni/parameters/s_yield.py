"""S_yield - Spin Quantum Yield parameter.

Measures photon-to-radical-pair conversion efficiency.
Φ_RP = k_ET / (k_ET + k_rec)
"""

from typing import Optional, Dict
import numpy as np


class SpinQuantumYield:
    """S_yield: Spin Quantum Yield.
    
    Attributes:
        phi_rp: Measured quantum yield (0-1)
        k_et: Forward electron transfer rate [s⁻¹]
        k_rec: Geminate recombination rate [s⁻¹]
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.phi_rp = None
        self.k_et = None
        self.k_rec = None
        
    def compute(self, phi_rp: float) -> float:
        """Compute normalized S_yield value."""
        # Normalize to theoretical maximum (0.97)
        normalized = min(phi_rp / 0.97, 1.0)
        return normalized
    
    def validate(self) -> bool:
        """Validate parameter calculation."""
        return 0 <= self.phi_rp <= 1 if self.phi_rp else False
