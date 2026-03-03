#!/usr/bin/env python3
"""Run all SPIMAG tests."""

import unittest
import sys
import os


def run_all_tests():
    """Discover and run all tests."""
    # Add src to path
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
    # Discover tests
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir, pattern="test_*.py")
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 60)
    print("🧪 Running all SPIMAG tests")
    print("=" * 60)
    
    success = run_all_tests()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed")
    print("=" * 60)
    
    sys.exit(0 if success else 1)
