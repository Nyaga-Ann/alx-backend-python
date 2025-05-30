#!/usr/bin/env python3
"""Unit test for utils.access_nested_map and utils.get_json"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns correct value"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises a KeyError with the expected message
        when accessing a non-existent key in the nested_map.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        missing_key = path[-1]
        self.assertEqual(str(context.exception), repr(missing_key))


class TestGetJson(unittest.TestCase):
    """Test cases for utils.get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns expected payload and requests.get called once"""
        # Configure the mock to return a response with json method returning test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json with the test_url
        result = get_json(test_url)

        # Assert requests.get was called once with test_url
        mock_get.assert_called_once_with(test_url)

        # Assert the result equals the expected test_payload
        self.assertEqual(result, test_payload)
