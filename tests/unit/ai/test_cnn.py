"""Unit tests for CNN spatial model."""

import unittest
import sys
import os
import torch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.ai.cnn_spatial import CNNSpatialPattern


class TestCNN(unittest.TestCase):
    """Test suite for CNN model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.cnn = CNNSpatialPattern(input_channels=1, num_classes=5)
        
    def test_model_creation(self):
        """Test model initialization."""
        self.assertIsNotNone(self.cnn)
        
    def test_forward_pass(self):
        """Test forward pass with random image."""
        batch_size = 2
        x = torch.randn(batch_size, 1, 32, 32)
        
        output = self.cnn(x)
        self.assertEqual(output.shape, (batch_size, 5))
        
    def test_prediction(self):
        """Test prediction method."""
        x = torch.randn(1, 1, 32, 32)
        pred = self.cnn.predict(x)
        self.assertEqual(pred.shape, (1, 5))


if __name__ == '__main__':
    unittest.main()
