#!/usr/bin/env python3
"""
Test GithubOrgClient.org with parameterized inputs and mock
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient.org method"""

    @parameterized.expand([
        ("google", "google"),
        ("abc", "abc"),
    ])
    @patch("client.get_json")
    def test_org(self, name, org_name, mock_get_json):
        """Test that .org returns expected data"""
        test_payload = {"login": org_name, "id": 123}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, test_payload)
