#!/usr/bin/env python3
"""
Testing GithubOrgClient.org method with parameterized inputs and mock
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
    def test_org(self, org_name):
        """Test GithubOrgClient.org returns expected data and calls get_json"""
        fake_response = {"name": org_name, "id": 42}

        with patch("client.get_json", return_value=fake_response) as mock_get:
            client = GithubOrgClient(org_name)
            result = client.org

            expected_url = f"https://api.github.com/orgs/{org_name}"
            mock_get.assert_called_once_with(expected_url)
            self.assertEqual(result, fake_response)
