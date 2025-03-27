#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for GithubOrgClient.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mock_get_json) -> None:
        """
        Test that GithubOrgClient.org returns the correct value.
        Test that get_json is called once with the expected URL.
        """
        fake_payload = {"login": org, "id": 123}
        mock_get_json.return_value = fake_payload

        client_instance = GithubOrgClient(org)
        result = client_instance.org
        expected_url = f"https://api.github.com/orgs/{org}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, fake_payload)

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns the correct repos_url from org.
        """
        test_url = "https://api.github.com/orgs/test-org/repos"
        mock_org_dict = {"repos_url": test_url}

        # Patch the .org property to return a real dict
        with patch.object(GithubOrgClient, "org", new=mock_org_dict):
            client = GithubOrgClient("test-org")
            result = client._public_repos_url
            self.assertEqual(result, test_url)


if __name__ == "__main__":
    unittest.main()
