"""Γ_coh - Quantum Coherence Lifetime parameter.

Duration of singlet-triplet quantum coherence.
τ_coh = -1 / Re(λ_relax)
"""

from typing import Optional, Dict
import numpy as np


class QuantumCoherenceLifetime:
    """Γ_coh: Quantum Coherence Lifetime.
    
    Attributes:
        tau_coh: Coherence lifetime [s]
        threshold: Minimum lifetime for <5° precision (4.7e-6 s)
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.tau_coh = None
        self.threshold = 4.7e-6  # 4.7 µs
        
    def compute(self, tau_coh: float) -> float:
        """Compute normalized Γ_coh value."""
        self.tau_coh = tau_coh
        normalized = min(tau_coh / self.threshold, 1.0)
        return normalized
    
    def validate(self) -> bool:
        """Validate parameter calculation."""
        return self.tau_coh >= 0 if self.tau_coh else False
