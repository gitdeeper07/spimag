"""θ_inc - Magnetic Inclination Sensitivity parameter.

Angular resolution for geomagnetic inclination.
θ_inc = arctan(Bz / √(Bx² + By²))
"""

from typing import Optional, Dict
import numpy as np


class MagneticInclinationSensitivity:
    """θ_inc: Magnetic Inclination Sensitivity.
    
    Attributes:
        precision: Angular resolution [degrees]
        dP_dtheta: Derivative of singlet yield with inclination
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.precision = None
        self.dP_dtheta = None
        
    def compute(self, precision: float) -> float:
        """Compute normalized θ_inc value."""
        self.precision = precision
        # Better precision = smaller angle = higher score
        normalized = max(0, 1 - (precision / 10.0))
        return min(normalized, 1.0)
    
    def validate(self) -> bool:
        """Validate parameter calculation."""
        return self.precision is not None
