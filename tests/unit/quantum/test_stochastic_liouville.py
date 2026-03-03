"""Unit tests for Stochastic Liouville solver."""

import unittest
import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.quantum.stochastic_liouville import StochasticLiouvilleSolver


class TestStochasticLiouville(unittest.TestCase):
    """Test suite for Stochastic Liouville solver."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.solver = StochasticLiouvilleSolver()
        
    def test_hamiltonian_building(self):
        """Test Hamiltonian construction."""
        H = self.solver.build_hamiltonian(B0=50e-6)
        self.assertEqual(H.shape, (4, 4))
        
    def test_time_evolution(self):
        """Test time evolution."""
        H = self.solver.build_hamiltonian()
        t, rho_t = self.solver.solve(H, t_max=10e-6, n_steps=100)
        
        self.assertEqual(len(t), 100)
        self.assertEqual(len(rho_t), 100)
        self.assertEqual(rho_t[0].shape, (4, 4))


if __name__ == '__main__':
    unittest.main()
