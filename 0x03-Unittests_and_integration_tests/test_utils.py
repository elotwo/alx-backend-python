#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
     @parameterized.expand([
         nested_map={"a": 1}, path=("a",)
         nested_map={"a": {"b": 2}}, path=("a",)
         nested_map={"a": {"b": 2}}, path=("a", "b")
         ])

     def TestAccessNestedMap(self, nested_map, path, expected):
          result = access_nested_map(nested_map, path)
          self.assertEqual(result, expected)
          
if __name__ == '__main__':
    unittest.main()
