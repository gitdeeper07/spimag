"""Unit tests for Navigational Vector Precision parameter."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

try:
    from src.smni.parameters.v_nav import NavigationalVectorPrecision
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))
    from smni.parameters.v_nav import NavigationalVectorPrecision


class TestNavigationalVectorPrecision(unittest.TestCase):
    """Test suite for V_nav parameter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.v_nav = NavigationalVectorPrecision()
        
    def test_perfect_consensus(self):
        """Test perfect directional consensus."""
        headings = [0.0] * 10
        result = self.v_nav.compute(headings)
        self.assertAlmostEqual(result, 1.0)
        
    def test_random_orientation(self):
        """Test random orientation."""
        headings = np.random.uniform(0, 2*np.pi, 100).tolist()
        result = self.v_nav.compute(headings)
        self.assertLess(result, 0.3)
        
    def test_two_clusters(self):
        """Test bimodal distribution."""
        headings = [0.0] * 5 + [np.pi] * 5
        result = self.v_nav.compute(headings)
        self.assertLess(result, 0.1)


if __name__ == '__main__':
    unittest.main()
