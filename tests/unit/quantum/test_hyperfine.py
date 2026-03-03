"""Unit tests for hyperfine tensor library."""

import unittest
import sys
import os
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.quantum.hyperfine_tensors import HyperfineTensorLibrary


class TestHyperfineTensors(unittest.TestCase):
    """Test suite for hyperfine tensor library."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.lib = HyperfineTensorLibrary()
        
    def test_tensor_count(self):
        """Test number of tensors."""
        self.assertEqual(len(self.lib.tensors), 5)
        
    def test_tensor_shapes(self):
        """Test tensor shapes."""
        for name, tensor in self.lib.tensors.items():
            self.assertEqual(tensor.shape, (3, 3))
            
    def test_get_tensor(self):
        """Test retrieving tensors."""
        tensor = self.lib.get_tensor('FAD_N1')
        self.assertIsNotNone(tensor)
        
        tensor = self.lib.get_tensor('nonexistent')
        self.assertIsNone(tensor)


if __name__ == '__main__':
    unittest.main()
