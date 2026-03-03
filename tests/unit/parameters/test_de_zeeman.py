"""Unit tests for Zeeman Energy Splitting parameter."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

try:
    from src.smni.parameters.de_zeeman import ZeemanEnergySplitting
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))
    from smni.parameters.de_zeeman import ZeemanEnergySplitting


class TestZeemanEnergySplitting(unittest.TestCase):
    """Test suite for ΔE_zeeman parameter."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.zeeman = ZeemanEnergySplitting()
        
    def test_energy_calculation(self):
        """Test Zeeman energy calculation."""
        # At 50 µT, should be ~5.6e-27 J
        energy = self.zeeman.compute()
        self.assertAlmostEqual(energy, 1.0, places=2)
        
    def test_angular_dependence(self):
        """Test dependence on inclination angle."""
        energy_0 = self.zeeman.compute(theta=0)
        energy_90 = self.zeeman.compute(theta=np.pi/2)
        
        # At 90°, cos(90)=0 so energy should be 0
        self.assertAlmostEqual(energy_90, 0.0, places=2)
        
    def test_field_strength_dependence(self):
        """Test dependence on field strength."""
        energy_50 = self.zeeman.compute(B0=50e-6)
        energy_100 = self.zeeman.compute(B0=100e-6)
        
        # Double field = double energy
        self.assertAlmostEqual(energy_100 / energy_50, 2.0, places=1)


if __name__ == '__main__':
    unittest.main()
