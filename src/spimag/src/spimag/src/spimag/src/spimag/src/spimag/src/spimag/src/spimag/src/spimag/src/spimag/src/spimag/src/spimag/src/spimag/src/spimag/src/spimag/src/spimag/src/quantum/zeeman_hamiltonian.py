"""Zeeman Hamiltonian implementation.

Ĥ_Zeeman(θ,φ) = γₑ B₀ (Ŝₐz sinθ cosφ + Ŝₐy sinθ sinφ + Ŝₐz cosθ + same for Ŝᵦ)
"""

import numpy as np
from typing import Optional, Tuple


class ZeemanHamiltonian:
    """Zeeman interaction Hamiltonian."""
    
    def __init__(self):
        self.gamma_e = 1.7608e11  # rad s⁻¹ T⁻¹
        self.hbar = 1.0545718e-34  # J·s
        
    def build(self, B0: float = 50e-6, theta: float = 0, phi: float = 0) -> np.ndarray:
        """Build Zeeman Hamiltonian matrix."""
        # Pauli matrices
        sx = 0.5 * np.array([[0, 1], [1, 0]], dtype=complex)
        sy = 0.5 * np.array([[0, -1j], [1j, 0]], dtype=complex)
        sz = 0.5 * np.array([[1, 0], [0, -1]], dtype=complex)
        
        # Field components
        Bx = B0 * np.sin(theta) * np.cos(phi)
        By = B0 * np.sin(theta) * np.sin(phi)
        Bz = B0 * np.cos(theta)
        
        # Single electron Zeeman
        H_electron = self.gamma_e * self.hbar * (Bx*sx + By*sy + Bz*sz)
        
        # Two-electron system (tensor product)
        H_total = np.kron(H_electron, np.eye(2)) + np.kron(np.eye(2), H_electron)
        
        return H_total
    
    def get_energy_splitting(self, B0: float = 50e-6) -> float:
        """Get Zeeman energy splitting ΔE = γₑ ℏ B₀."""
        return self.gamma_e * self.hbar * B0
