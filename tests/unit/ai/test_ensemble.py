"""Unit tests for ensemble model."""

import unittest
import sys
import os
import numpy as np
import torch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.ai.ensemble import SMNIEnsemble
from src.ai.lstm_detector import LSTMSpinDetector
from src.ai.xgboost_classifier import XGBoostSMNIClassifier
from src.ai.cnn_spatial import CNNSpatialPattern
from src.ai.pi_qnn import PhysicsInformedQNN


class TestEnsemble(unittest.TestCase):
    """Test suite for ensemble model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.ensemble = SMNIEnsemble()
        
        # Add mock models
        self.ensemble.add_model('lstm', LSTMSpinDetector(input_dim=10, hidden_dim=32))
        self.ensemble.add_model('xgboost', XGBoostSMNIClassifier())
        self.ensemble.add_model('cnn', CNNSpatialPattern())
        self.ensemble.add_model('pi_qnn', PhysicsInformedQNN(input_dim=8, hidden_dim=32))
        
    def test_ensemble_weights(self):
        """Test ensemble weights."""
        self.assertAlmostEqual(sum(self.ensemble.weights.values()), 1.0)
        
    def test_prediction_without_models(self):
        """Test prediction with no data."""
        result = self.ensemble.predict({})
        self.assertEqual(result[0], 0.0)  # SMNI score


if __name__ == '__main__':
    unittest.main()
