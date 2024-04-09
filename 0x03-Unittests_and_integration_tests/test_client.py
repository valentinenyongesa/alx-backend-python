#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient
"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to test GithubOrgClient class
    """

    def test_public_repos_url(self):
        """
        Test GithubOrgClient._public_repos_url method
        """
        # Define a known payload
        payload = {"repos_url": "https://api.github.com/orgs/test/repos"}

        # Patch GithubOrgClient.org to return known payload
        with patch('client.GithubOrgClient.org', return_value=payload):
            # Create instance of GithubOrgClient
            client = GithubOrgClient('test')

            # Retrieve public repos URL
            public_repos_url = client._public_repos_url

            # Assert that the public repos URL is the expected one
            self.assertEqual(
                    public_repos_url, "https://api.github.com/orgs/test/repos"
            )


if __name__ == '__main__':
    unittest.main()
