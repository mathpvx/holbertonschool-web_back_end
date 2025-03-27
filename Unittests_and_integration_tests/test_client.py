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

        with patch.object(GithubOrgClient, "org", new=mock_org_dict):
            client = GithubOrgClient("test-org")
            result = client._public_repos_url
            self.assertEqual(result, test_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test that public_repos returns expected list of repo names.
        Also test get_json and _public_repos_url are called once.
        """
        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = mock_repos_payload

        test_url = "https://api.github.com/orgs/test-org/repos"

        with patch.object(GithubOrgClient, "_public_repos_url", new=test_url):
            client = GithubOrgClient("test-org")
            result = client.public_repos()

            expected_result = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_result)

            mock_get_json.assert_called_once_with(test_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license returns correct boolean.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
