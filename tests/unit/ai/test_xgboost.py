"""Unit tests for XGBoost classifier."""

import unittest
import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.ai.xgboost_classifier import XGBoostSMNIClassifier


class TestXGBoostClassifier(unittest.TestCase):
    """Test suite for XGBoost classifier."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.xgb = XGBoostSMNIClassifier()
        
    def test_initialization(self):
        """Test initialization."""
        self.assertIsNotNone(self.xgb)
        self.assertEqual(len(self.xgb.feature_names), 8)
        
    def test_training(self):
        """Test training with random data."""
        X = np.random.rand(100, 8)
        y = np.random.randint(0, 5, 100)
        
        self.xgb.train(X, y)
        self.assertIsNotNone(self.xgb.model)
        
    def test_prediction(self):
        """Test prediction."""
        X = np.random.rand(10, 8)
        y = np.random.randint(0, 5, 10)
        
        self.xgb.train(X, y)
        pred = self.xgb.predict(X)
        self.assertEqual(pred.shape, (10,))


if __name__ == '__main__':
    unittest.main()
