#!/usr/bin/env python3

"""
Integration tests for GithubOrgClient class
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
                     [(org_payload(), repos_payload(), expected_repos(), apache2_repos())])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class
        """
        cls.get_patcher = patch('client.requests.get')

        # Start patcher and mock requests.get with side_effect
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = [cls.org_payload, cls.repos_payload]

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test class
        """
        # Stop patcher
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method
        """
        # Create instance of GithubOrgClient
        client = GithubOrgClient('test')

        # Call public_repos method
        repos = client.public_repos()

        # Assert that the result is as expected
        self.assertEqual(repos, self.expected_repos)


if __name__ == '__main__':
    unittest.main()
