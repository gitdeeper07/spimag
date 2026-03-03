"""Coherence lifetime estimation from decay curves."""

import numpy as np
from typing import Optional, Tuple
from scipy.optimize import curve_fit


class CoherenceEstimation:
    """Estimate coherence lifetime from decay curves."""
    
    def __init__(self):
        pass
    
    def exponential_decay(self, t: np.ndarray, tau: float, a: float, c: float) -> np.ndarray:
        """Exponential decay model: a * exp(-t/tau) + c."""
        return a * np.exp(-t / tau) + c
    
    def estimate_tau(self, t: np.ndarray, signal: np.ndarray) -> float:
        """Estimate coherence lifetime from decay curve."""
        # Initial guess
        a0 = signal[0] - signal[-1]
        c0 = signal[-1]
        tau0 = (t[-1] - t[0]) / 4
        
        try:
            popt, _ = curve_fit(
                self.exponential_decay, t, signal,
                p0=[tau0, a0, c0],
                bounds=(0, [100e-6, 2*a0, 2*c0])
            )
            return popt[0]  # tau
        except:
            # Fallback to simple estimation
            half_max_idx = np.argmin(np.abs(signal - signal[0]/2))
            return t[half_max_idx]
