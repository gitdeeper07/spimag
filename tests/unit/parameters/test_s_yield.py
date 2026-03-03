"""Unit tests for Spin Quantum Yield parameter."""

import unittest
import sys
import os

# إضافة المسار بشكل صحيح
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

try:
    from src.smni.parameters.s_yield import SpinQuantumYield
except ImportError:
    # محاولة بديلة
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))
    from smni.parameters.s_yield import SpinQuantumYield


class TestSpinQuantumYield(unittest.TestCase):
    """Test suite for S_yield parameter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.s_yield = SpinQuantumYield()
        
    def test_compute_normal(self):
        """Test normal computation range."""
        result = self.s_yield.compute(0.85)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 1)
        
    def test_compute_edge_cases(self):
        """Test edge cases."""
        # Maximum
        result = self.s_yield.compute(0.97)
        self.assertAlmostEqual(result, 1.0, places=2)
        
        # Minimum
        result = self.s_yield.compute(0.0)
        self.assertEqual(result, 0.0)
        
    def test_validation(self):
        """Test parameter validation."""
        self.s_yield.phi_rp = 0.85
        self.assertTrue(self.s_yield.validate())
        
        self.s_yield.phi_rp = 1.5
        self.assertFalse(self.s_yield.validate())


if __name__ == '__main__':
    unittest.main()
