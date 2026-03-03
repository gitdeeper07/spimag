"""Harmonic regression for seasonal cycle removal."""

import numpy as np
from typing import Optional, Tuple
from scipy.optimize import least_squares


class HarmonicRegression:
    """Remove seasonal cycles using harmonic regression."""
    
    def __init__(self, n_harmonics: int = 3):
        self.n_harmonics = n_harmonics
        self.params = None
        
    def harmonic_model(self, t: np.ndarray, params: np.ndarray) -> np.ndarray:
        """Harmonic model: Σ [a_i * sin(2πi t) + b_i * cos(2πi t)]."""
        result = np.zeros_like(t, dtype=float)
        
        for i in range(self.n_harmonics):
            a = params[2*i]
            b = params[2*i + 1]
            result += a * np.sin(2 * np.pi * (i+1) * t)
            result += b * np.cos(2 * np.pi * (i+1) * t)
            
        return result
    
    def fit(self, t: np.ndarray, data: np.ndarray) -> np.ndarray:
        """Fit harmonic model to data."""
        def residuals(params):
            return data - self.harmonic_model(t, params)
        
        # Initial guess
        x0 = np.zeros(2 * self.n_harmonics)
        
        # Optimize
        result = least_squares(residuals, x0)
        self.params = result.x
        
        return self.params
    
    def predict(self, t: np.ndarray) -> np.ndarray:
        """Predict seasonal component."""
        if self.params is None:
            raise ValueError("Model not fitted")
        return self.harmonic_model(t, self.params)
    
    def remove_seasonal(self, t: np.ndarray, data: np.ndarray) -> np.ndarray:
        """Remove seasonal component from data."""
        if self.params is None:
            self.fit(t, data)
        seasonal = self.predict(t)
        return data - seasonal
