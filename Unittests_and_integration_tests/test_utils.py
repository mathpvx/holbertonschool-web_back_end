#!/usr/bin/env python3

"""
test access_nested_map function with different nested structures
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ("case1", {'a': 1}, ('a',), 1),
        ("case2", {'a': {'b': 2}}, ('a',), {'b': 2}),
        ("case3", {'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, _, nested_map, path, expected):
        self.assertEqual(
            access_nested_map(nested_map, path), expected
        )
