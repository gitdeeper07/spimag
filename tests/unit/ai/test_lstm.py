"""Unit tests for LSTM detector."""

import unittest
import sys
import os
import torch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.ai.lstm_detector import LSTMSpinDetector


class TestLSTMDetector(unittest.TestCase):
    """Test suite for LSTM detector."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.lstm = LSTMSpinDetector(input_dim=10, hidden_dim=32, num_layers=1)
        
    def test_model_creation(self):
        """Test model initialization."""
        self.assertIsNotNone(self.lstm)
        self.assertEqual(self.lstm.hidden_dim, 32)
        
    def test_forward_pass(self):
        """Test forward pass with random data."""
        batch_size = 5
        seq_len = 20
        x = torch.randn(batch_size, seq_len, 10)
        
        output = self.lstm(x)
        self.assertEqual(output.shape, (batch_size, 1))
        
    def test_prediction(self):
        """Test prediction method."""
        x = torch.randn(1, 20, 10)
        pred = self.lstm.predict(x)
        self.assertEqual(pred.shape, (1, 1))


if __name__ == '__main__':
    unittest.main()
