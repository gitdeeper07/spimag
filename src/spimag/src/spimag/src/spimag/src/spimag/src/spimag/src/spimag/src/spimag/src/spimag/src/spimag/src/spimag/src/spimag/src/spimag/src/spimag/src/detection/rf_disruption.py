"""RF interference detection module."""

import numpy as np
from typing import Optional, Dict, Tuple


class RFDisruptionDetector:
    """Detect RF interference effects on magnetoreception."""
    
    def __init__(self):
        self.proton_larmor = 1.4e6  # Hz at 50 µT
        
    def disruption_risk(self, rf_freq: float, rf_amplitude: float, 
                        distance_km: float) -> float:
        """Calculate disruption risk score."""
        # Frequency match factor
        freq_ratio = min(rf_freq / self.proton_larmor, 
                        self.proton_larmor / rf_freq)
        freq_factor = np.exp(-(1 - freq_ratio)**2 / 0.1)
        
        # Amplitude factor (1 nT threshold)
        amp_factor = min(rf_amplitude / 1e-9, 1.0)
        
        # Distance factor (inverse square)
        dist_factor = 1 / (1 + (distance_km / 10)**2)
        
        risk = freq_factor * amp_factor * dist_factor
        return min(risk, 1.0)
    
    def is_disrupted(self, smni: float, threshold: float = 0.4) -> bool:
        """Check if navigation is disrupted."""
        return smni < threshold
