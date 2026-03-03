"""P_singlet - Singlet-Triplet State Probability parameter.

Primary output variable encoding directional information.
P_S(t) = Tr[P̂_S ρ(t)]
"""

from typing import Optional, Dict
import numpy as np


class SingletTripletProbability:
    """P_singlet: Singlet-Triplet State Probability.
    
    Attributes:
        p_singlet: Probability of singlet state [0-1]
        delta_phi: Magnetic field effect on yield
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.p_singlet = None
        self.delta_phi = None
        
    def compute(self, p_singlet: float) -> float:
        """Compute normalized P_singlet value."""
        self.p_singlet = p_singlet
        # Higher singlet probability = stronger signal
        return min(p_singlet, 1.0)
    
    def validate(self) -> bool:
        """Validate parameter calculation."""
        return 0 <= self.p_singlet <= 1 if self.p_singlet else False
