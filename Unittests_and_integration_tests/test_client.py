#!/usr/bin/env python3
"""
Testing GithubOrgClient.org method with mock and parameterized inputs
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        # Setup: fake payload returned by get_json
        fake_response = {"name": org_name, "id": 42}
        mock_get.return_value = fake_response

        # Create client and call .org()
        client = GithubOrgClient(org_name)
        result = client.org

        # Make sure get_json was called once with correct URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get.assert_called_once_with(expected_url)

        # Check if result matches what we mocked
        self.assertEqual(result, fake_response)
