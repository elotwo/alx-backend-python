#!/usr/bin/env python3
"""
unit testing
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    unit test
    """
    @parameterized.expand([
        ({"a":1}, ("a",), 1),
        ({"a": {"b":2}}, ("a",), {"b":2}),
        ({"a": {"b":2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        testing
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"]),
    ])

    def test_access_nested_map_exception(self,nested_map,key_sequence):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, key_sequence)



if __name__ == '__main__':
    unittest.main()
