#!/usr/bin/env python3
"""
Unit tests for utils.memoize
"""
import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """
    Class to test memoize decorator
    """

    class TestClass:
        """
        Class with a_method and memoized a_property
        """
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch('utils.TestMemoize.TestClass.a_method')
    def test_memoize(self, mock_a_method):
        """
        Test memoize decorator
        """
        instance = self.TestClass()

        # Call a_property twice
        result1 = instance.a_property()
        result2 = instance.a_property()

        # Assert that a_method was called only once
        mock_a_method.assert_called_once()

        # Assert that the results are correct
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
