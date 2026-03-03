"""Unit tests for Paramagnetic Susceptibility parameter."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

try:
    from src.smni.parameters.chi_para import ParamagneticSusceptibility
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))
    from smni.parameters.chi_para import ParamagneticSusceptibility


class TestParamagneticSusceptibility(unittest.TestCase):
    """Test suite for χ_para parameter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.chi = ParamagneticSusceptibility()
        
    def test_magnetite_moment(self):
        """Test magnetite moment value."""
        self.assertAlmostEqual(self.chi.mu, 1.4e-17, delta=1e-18)
        
    def test_compute(self):
        """Test computation."""
        result = self.chi.compute(0.8)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
