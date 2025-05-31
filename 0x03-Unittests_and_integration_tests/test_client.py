#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct value"""
        test_payload = {'login': org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL from org payload"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            expected_url = "https://api.github.com/orgs/google/repos"
            mock_org.return_value = {"repos_url": expected_url}

            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, expected_url)
