# test_ordersync.py
"""
Tests for OrderSync module.
"""

import unittest
from ordersync import OrderSync

class TestOrderSync(unittest.TestCase):
    """Test cases for OrderSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OrderSync()
        self.assertIsInstance(instance, OrderSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OrderSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
