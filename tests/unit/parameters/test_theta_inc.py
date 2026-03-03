"""Unit tests for Magnetic Inclination Sensitivity parameter."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

try:
    from src.smni.parameters.theta_inc import MagneticInclinationSensitivity
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))
    from smni.parameters.theta_inc import MagneticInclinationSensitivity


class TestMagneticInclinationSensitivity(unittest.TestCase):
    """Test suite for θ_inc parameter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.theta = MagneticInclinationSensitivity()
        
    def test_precision_scoring(self):
        """Test precision scoring."""
        # 1° precision = high score
        score_1 = self.theta.compute(1.0)
        
        # 5° precision = medium score
        score_5 = self.theta.compute(5.0)
        
        # 10° precision = low score
        score_10 = self.theta.compute(10.0)
        
        self.assertGreater(score_1, score_5)
        self.assertGreater(score_5, score_10)
        
    def test_range(self):
        """Test output range."""
        for prec in [0.5, 2.0, 5.0, 8.0, 12.0]:
            score = self.theta.compute(prec)
            self.assertGreaterEqual(score, 0)
            self.assertLessEqual(score, 1)


if __name__ == '__main__':
    unittest.main()
