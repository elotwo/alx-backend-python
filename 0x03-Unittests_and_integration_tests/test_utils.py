#!/usr/bin/env python3
"""
unit testing
"""
import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    unit test
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        testing
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, nested_map, key_sequence):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, key_sequence)


class TestGetJson(unittest.TestCase):

    def test_get_json(self):
        """Test that get_json returns the expected result."""
        test_url = "http://example.com"
        test_payload = {"key": "value"}

        # Mocking requests.get
        with patch("utils.requests.get") as mock_get:
            # Create a mock response object with a json method
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function with the test URL
            result = get_json(test_url)

            # Assert that the json result matches the test payload
            self.assertEqual(result, test_payload)

            # Assert that requests.get was called once with the test URL
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        """Test that the memoize decorator caches method calls."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        expected_result = {"login": org_name}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_result)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url
        returns the correct value.
        """
        test_payload = {"repos_url":
                        "https://api.github.com/orgs/test-org/repos"}
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = test_payload
            client = GithubOrgClient("test-org")
            result = client._public_repos_url
            self.assertEqual(result, test_payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos
        returns the expected list of repos.
        """
        test_payload = ["repo1", "repo2", "repo3"]
        mock_get_json.return_value = test_payload
        test_url = "https://api.github.com/orgs/test-org/repos"

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_url
            client = GithubOrgClient("test-org")
            result = client.public_repos

            self.assertEqual(result, test_payload)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(test_url)


@parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
def test_has_license(self, repo, license_key, expected_result):
    """Test that GithubOrgClient.has_license
    checks for the correct license key.
    """
    client = GithubOrgClient("test-org")
    result = client.has_license(repo, license_key)
    self.assertEqual(result, expected_result)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up class-level mocks for requests.get."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def get_side_effect(url):
            if url == "https://api.github.com/orgs/test-org":
                return cls.MockResponse(cls.org_payload)
            elif url == "https://api.github.com/orgs/test-org/repos":
                return cls.MockResponse(cls.repos_payload)
            return cls.MockResponse(None)

        cls.mock_get.side_effect = lambda url: get_side_effect(url)

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data


if __name__ == '__main__':
    unittest.main()
