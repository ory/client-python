"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.1.34
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_client
from ory_client.api.oidc_api import OidcApi  # noqa: E501


class TestOidcApi(unittest.TestCase):
    """OidcApi unit test stubs"""

    def setUp(self):
        self.api = OidcApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_oidc_dynamic_client(self):
        """Test case for create_oidc_dynamic_client

        Register OAuth2 Client using OpenID Dynamic Client Registration  # noqa: E501
        """
        pass

    def test_delete_oidc_dynamic_client(self):
        """Test case for delete_oidc_dynamic_client

        Delete OAuth 2.0 Client using the OpenID Dynamic Client Registration Management Protocol  # noqa: E501
        """
        pass

    def test_discover_oidc_configuration(self):
        """Test case for discover_oidc_configuration

        OpenID Connect Discovery  # noqa: E501
        """
        pass

    def test_get_oidc_dynamic_client(self):
        """Test case for get_oidc_dynamic_client

        Get OAuth2 Client using OpenID Dynamic Client Registration  # noqa: E501
        """
        pass

    def test_get_oidc_user_info(self):
        """Test case for get_oidc_user_info

        OpenID Connect Userinfo  # noqa: E501
        """
        pass

    def test_revoke_oidc_session(self):
        """Test case for revoke_oidc_session

        OpenID Connect Front- and Back-channel Enabled Logout  # noqa: E501
        """
        pass

    def test_set_oidc_dynamic_client(self):
        """Test case for set_oidc_dynamic_client

        Set OAuth2 Client using OpenID Dynamic Client Registration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
