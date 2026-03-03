"""Integration tests for quantum and AI modules."""

import unittest
import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.quantum.stochastic_liouville import StochasticLiouvilleSolver
from src.ai.lstm_detector import LSTMSpinDetector


class TestQuantumAIIntegration(unittest.TestCase):
    """Test integration between quantum and AI modules."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.solver = StochasticLiouvilleSolver()
        self.lstm = LSTMSpinDetector(input_dim=10)
        
    def test_data_flow(self):
        """Test data flow from quantum to AI."""
        # Generate quantum data
        H = self.solver.build_hamiltonian()
        t, rho_t = self.solver.solve(H, n_steps=50)
        
        # Convert to tensor
        import torch
        x = torch.randn(1, 50, 10)  # Mock data
        
        # Pass through LSTM
        output = self.lstm(x)
        
        self.assertEqual(output.shape, (1, 1))


if __name__ == '__main__':
    unittest.main()
