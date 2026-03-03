"""Unit tests for Physics-Informed QNN."""

import unittest
import sys
import os
import torch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.ai.pi_qnn import PhysicsInformedQNN


class TestPIQNN(unittest.TestCase):
    """Test suite for PI-QNN model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.qnn = PhysicsInformedQNN(input_dim=8, hidden_dim=32, quantum_layers=1)
        
    def test_model_creation(self):
        """Test model initialization."""
        self.assertIsNotNone(self.qnn)
        self.assertEqual(self.qnn.quantum_layers, 1)
        
    def test_forward_pass(self):
        """Test forward pass."""
        batch_size = 3
        x = torch.randn(batch_size, 8)
        
        output = self.qnn(x)
        self.assertEqual(output.shape, (batch_size, 5))
        
    def test_zeeman_constraint(self):
        """Test physics constraint computation."""
        x = torch.randn(5, 8)
        penalty = self.qnn.compute_zeeman_constraint(x)
        self.assertEqual(penalty.shape, (5,))


if __name__ == '__main__':
    unittest.main()
