"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.1.25
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_client
from ory_client.api.jwk_api import JwkApi  # noqa: E501


class TestJwkApi(unittest.TestCase):
    """JwkApi unit test stubs"""

    def setUp(self):
        self.api = JwkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_json_web_key_set(self):
        """Test case for create_json_web_key_set

        Create JSON Web Key  # noqa: E501
        """
        pass

    def test_delete_json_web_key(self):
        """Test case for delete_json_web_key

        Delete JSON Web Key  # noqa: E501
        """
        pass

    def test_delete_json_web_key_set(self):
        """Test case for delete_json_web_key_set

        Delete JSON Web Key Set  # noqa: E501
        """
        pass

    def test_get_json_web_key(self):
        """Test case for get_json_web_key

        Get JSON Web Key  # noqa: E501
        """
        pass

    def test_get_json_web_key_set(self):
        """Test case for get_json_web_key_set

        Retrieve a JSON Web Key Set  # noqa: E501
        """
        pass

    def test_set_json_web_key(self):
        """Test case for set_json_web_key

        Set JSON Web Key  # noqa: E501
        """
        pass

    def test_set_json_web_key_set(self):
        """Test case for set_json_web_key_set

        Update a JSON Web Key Set  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
