#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to test GithubOrgClient class
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test GithubOrgClient.org method
        """
        # Instantiate GithubOrgClient with org_name
        client = GithubOrgClient(org_name)

        # Call org method
        client.org()

        # Assert that get_json was called once with the correct argument
        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{org_name}'
                )


if __name__ == '__main__':
    unittest.main()
