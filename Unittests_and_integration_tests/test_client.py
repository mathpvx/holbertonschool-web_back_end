#!/usr/bin/env python3
"""
Test GithubOrgClient.org with parameterized expand and patch
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient.org"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    def test_org(self, org_name):
        """Test org method returns correct payload"""
        test_payload = {"name": org_name, "id": 123}

        with patch("client.get_json", return_value=test_payload) as mock_get_json:
            client = GithubOrgClient(org_name)
            result = client.org

            mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
            )
            self.assertEqual(result, test_payload)
