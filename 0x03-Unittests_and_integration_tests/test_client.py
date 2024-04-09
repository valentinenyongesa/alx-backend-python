#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient
"""
import unittest
from unittest.mock import patch, MagicMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to test GithubOrgClient class
    """

    def test_public_repos(self):
        """
        Test GithubOrgClient.public_repos method
        """
        # Define a known payload
        payload = [{"name": "repo1"}, {"name": "repo2"}]

        # Mocking get_json
        with patch(
                'client.GithubOrgClient.get_json', return_value=payload
        ) as mock_get_json:
            # Mocking _public_repos_url
            with patch(
                    'client.GithubOrgClient._public_repos_url',
                    return_value="https://example.com"
            ) as mock_public_repos_url:
                # Create instance of GithubOrgClient
                client = GithubOrgClient('test')

                # Call public_repos method
                repos = client.public_repos()

                # Assert that get_json was called once
                mock_get_json.assert_called_once()

                # Assert that _public_repos_url was called once
                mock_public_repos_url.assert_called_once()

                # Assert the result is as expected
                self.assertEqual(repos, payload)


if __name__ == '__main__':
    unittest.main()
