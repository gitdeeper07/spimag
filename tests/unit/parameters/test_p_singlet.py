"""Unit tests for Singlet-Triplet Probability parameter."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

try:
    from src.smni.parameters.p_singlet import SingletTripletProbability
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))
    from smni.parameters.p_singlet import SingletTripletProbability


class TestSingletTripletProbability(unittest.TestCase):
    """Test suite for P_singlet parameter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.p_singlet = SingletTripletProbability()
        
    def test_compute(self):
        """Test computation."""
        result = self.p_singlet.compute(0.5)
        self.assertEqual(result, 0.5)
        
        result = self.p_singlet.compute(1.0)
        self.assertEqual(result, 1.0)
        
    def test_validation(self):
        """Test parameter validation."""
        self.p_singlet.p_singlet = 0.7
        self.assertTrue(self.p_singlet.validate())
        
        self.p_singlet.p_singlet = 1.2
        self.assertFalse(self.p_singlet.validate())


if __name__ == '__main__':
    unittest.main()
