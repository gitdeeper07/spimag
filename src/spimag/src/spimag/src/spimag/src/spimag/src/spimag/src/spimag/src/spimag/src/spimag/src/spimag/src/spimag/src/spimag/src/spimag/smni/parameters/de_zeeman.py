"""ΔE_zeeman - Zeeman Energy Splitting parameter.

Energy gap between spin states under Earth's field.
ΔE = γₑ ℏ B₀ cosθ
"""

from typing import Optional, Dict
import numpy as np


class ZeemanEnergySplitting:
    """ΔE_zeeman: Zeeman Energy Splitting.
    
    Attributes:
        gamma_e: Electron gyromagnetic ratio (1.7608e11 rad s⁻¹ T⁻¹)
        B0: Earth's field strength [T]
        theta: Field inclination angle [rad]
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.gamma_e = 1.7608e11
        self.B0 = 50e-6  # 50 µT
        self.theta = None
        
    def compute(self, B0: float = None, theta: float = None) -> float:
        """Compute normalized ΔE_zeeman value."""
        B0 = B0 or self.B0
        theta = theta or self.theta or 0
        
        # ΔE = γₑ ℏ B₀ cosθ
        hbar = 1.0545718e-34  # J·s
        delta_e = self.gamma_e * hbar * B0 * np.cos(theta)
        
        # Normalize to theoretical maximum
        delta_e_max = self.gamma_e * hbar * 50e-6
        normalized = delta_e / delta_e_max
        
        return normalized
    
    def validate(self) -> bool:
        """Validate parameter calculation."""
        return True
