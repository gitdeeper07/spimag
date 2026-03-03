"""V_nav - Navigational Vector Precision parameter.

Final heading accuracy from population integration.
V_nav = R · exp(iΘ_mean) where R = |Σⱼ exp(iΘⱼ)| / N
"""

from typing import Optional, Dict, List
import numpy as np


class NavigationalVectorPrecision:
    """V_nav: Navigational Vector Precision.
    
    Attributes:
        R: Mean resultant vector length [0-1]
        theta_mean: Mean heading direction [rad]
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.R = None
        self.theta_mean = None
        
    def compute(self, headings: List[float]) -> float:
        """Compute V_nav from list of headings [radians]."""
        if not headings:
            return 0.0
            
        # Calculate mean resultant vector
        x = np.mean(np.cos(headings))
        y = np.mean(np.sin(headings))
        
        self.R = np.sqrt(x**2 + y**2)
        self.theta_mean = np.arctan2(y, x)
        
        return self.R
    
    def validate(self) -> bool:
        """Validate parameter calculation."""
        return 0 <= self.R <= 1 if self.R is not None else False
