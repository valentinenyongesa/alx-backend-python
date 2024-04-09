#!/usr/bin/env python3

"""
Integration tests for GithubOrgClient class
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment
        """
        cls.org_payload = org_payload()
        cls.repos_payload = repos_payload()
        cls.expected_repos = expected_repos()
        cls.apache2_repos = apache2_repos()

    def test_public_repos(self):
        """
        Test public_repos method without license argument
        """
        with patch('client.GithubOrgClient.org', return_value=self.org_payload), \
             patch('client.GithubOrgClient._public_repos_url'), \
             patch('client.GithubOrgClient.get_json', return_value=self.repos_payload):
            client = GithubOrgClient('test')
            repos = client.public_repos()
            self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with license argument
        """
        with patch('client.GithubOrgClient.org', return_value=self.org_payload), \
             patch('client.GithubOrgClient._public_repos_url'), \
             patch('client.GithubOrgClient.get_json', return_value=self.apache2_repos):
            client = GithubOrgClient('test')
            repos = client.public_repos(license='apache-2.0')
            self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
