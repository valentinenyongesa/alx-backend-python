#!/usr/bin/env python3

"""
Unit tests for client.GithubOrgClient
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to test GithubOrgClient class
    """

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test GithubOrgClient.has_license method
        """
        # Create instance of GithubOrgClient
        client = GithubOrgClient('test')

        # Call has_license method
        result = client.has_license(repo, license_key)

        # Assert that the result is as expected
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
