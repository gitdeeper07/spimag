"""Unit tests for Dipolar Coupling Tensor parameter."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

try:
    from src.smni.parameters.omega_dipole import DipolarCouplingTensor
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))
    from smni.parameters.omega_dipole import DipolarCouplingTensor


class TestDipolarCouplingTensor(unittest.TestCase):
    """Test suite for Ω_dipole parameter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.dipole = DipolarCouplingTensor()
        
    def test_distance_dependence(self):
        """Test dependence on inter-radical distance."""
        # Shorter distance = stronger coupling = lower score
        score_15a = self.dipole.compute(r=15e-10)
        score_20a = self.dipole.compute(r=20e-10)
        
        self.assertGreater(score_20a, score_15a)
        
    def test_erithacus_value(self):
        """Test European Robin known distance (19.5 Å)."""
        score = self.dipole.compute(r=19.5e-10)
        self.assertGreater(score, 0)
        self.assertLess(score, 1)


if __name__ == '__main__':
    unittest.main()
