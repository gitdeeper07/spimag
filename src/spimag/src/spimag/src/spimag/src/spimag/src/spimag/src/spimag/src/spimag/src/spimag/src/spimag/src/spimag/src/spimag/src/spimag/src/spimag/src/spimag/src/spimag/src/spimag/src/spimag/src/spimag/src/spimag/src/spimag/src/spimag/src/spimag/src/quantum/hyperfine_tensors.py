"""Hyperfine coupling tensor library."""

import numpy as np
from typing import Dict, List, Optional


class HyperfineTensorLibrary:
    """Library of hyperfine coupling tensors for cryptochrome."""
    
    def __init__(self):
        self.tensors = {}
        self._initialize_tensors()
        
    def _initialize_tensors(self):
        """Initialize default hyperfine tensors."""
        # FAD isoalloxazine ring nitrogen atoms
        self.tensors['FAD_N1'] = np.array([
            [2.1, 0.0, 0.0],
            [0.0, 2.1, 0.0],
            [0.0, 0.0, 3.5]
        ]) * 1e-3  # Tesla
        
        self.tensors['FAD_N3'] = np.array([
            [1.8, 0.0, 0.0],
            [0.0, 1.8, 0.0],
            [0.0, 0.0, 3.2]
        ]) * 1e-3
        
        self.tensors['FAD_N5'] = np.array([
            [1.5, 0.0, 0.0],
            [0.0, 1.5, 0.0],
            [0.0, 0.0, 2.8]
        ]) * 1e-3
        
        self.tensors['FAD_N10'] = np.array([
            [1.2, 0.0, 0.0],
            [0.0, 1.2, 0.0],
            [0.0, 0.0, 2.1]
        ]) * 1e-3
        
        # Tryptophan indole nitrogen
        self.tensors['Trp_N1'] = np.array([
            [2.5, 0.0, 0.0],
            [0.0, 2.5, 0.0],
            [0.0, 0.0, 4.2]
        ]) * 1e-3
    
    def get_tensor(self, name: str) -> np.ndarray:
        """Get hyperfine tensor by name."""
        return self.tensors.get(name)
    
    def get_all_tensors(self) -> Dict:
        """Get all hyperfine tensors."""
        return self.tensors
