"""Spin-selective recombination kinetics."""

import numpy as np
from typing import Optional, Tuple


class RecombinationKinetics:
    """Spin-selective recombination rates."""
    
    def __init__(self, k_s: float = 1e6, k_t: float = 1e4):
        self.k_s = k_s  # Singlet recombination rate [s⁻¹]
        self.k_t = k_t  # Triplet recombination rate [s⁻¹]
        
    def singlet_yield(self, rho_t: np.ndarray, t: np.ndarray) -> np.ndarray:
        """Calculate time-dependent singlet yield."""
        # Singlet projection operator
        P_s = np.zeros((4, 4), dtype=complex)
        P_s[0, 0] = 1.0
        
        phi_s = np.zeros_like(t, dtype=float)
        
        for i, ti in enumerate(t):
            # Φ_S(t) = ∫₀ᵗ k_S Tr[P̂_S ρ(t')] exp(-k_total t') dt'
            # Simplified: just singlet population
            rho = rho_t[i]
            phi_s[i] = np.real(np.trace(P_s @ rho))
        
        return phi_s
    
    def magnetic_field_effect(self, rho_t: np.ndarray, t: np.ndarray, 
                              rho_0: np.ndarray, t_0: np.ndarray) -> float:
        """Calculate magnetic field effect ΔΦ = Φ_S(B) − Φ_S(0)."""
        phi_B = self.singlet_yield(rho_t, t)
        phi_0 = self.singlet_yield(rho_0, t_0)
        
        return np.trapz(phi_B, t) - np.trapz(phi_0, t_0)
