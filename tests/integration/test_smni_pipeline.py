"""Integration tests for SMNI pipeline."""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.smni.composite import SMNIComposite
from src.smni.parameters import (
    s_yield, de_zeeman, gamma_coh, theta_inc,
    chi_para, p_singlet, omega_dipole, v_nav
)


class TestSMNIPipeline(unittest.TestCase):
    """Test complete SMNI pipeline."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.smni = SMNIComposite()
        
    def test_erithacus_rubecula(self):
        """Test European Robin known values."""
        params = {
            'S_yield': 0.92,
            'ΔE_zeeman': 0.88,
            'Γ_coh': 0.95,
            'θ_inc': 0.91,
            'χ_para': 0.45,
            'P_singlet': 0.87,
            'Ω_dipole': 0.82,
            'V_nav': 0.94
        }
        
        score = self.smni.compute(params)
        level = self.smni.get_alert_level(score)
        
        self.assertGreater(score, 0.8)
        self.assertIn(level, ['OPTIMAL', 'GOOD'])
        
    def test_invalid_params(self):
        """Test validation with invalid parameters."""
        params = {
            'S_yield': 1.5,  # Invalid >1
            'ΔE_zeeman': 0.88,
            'Γ_coh': 0.95,
        }
        
        valid = self.smni.validate_params(params)
        self.assertFalse(valid)


if __name__ == '__main__':
    unittest.main()
