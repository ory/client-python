"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.2.0-alpha.34
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_client
from ory_client.api.admin_api import AdminApi  # noqa: E501


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_consent_request(self):
        """Test case for accept_consent_request

        Accept a Consent Request  # noqa: E501
        """
        pass

    def test_accept_login_request(self):
        """Test case for accept_login_request

        Accept a Login Request  # noqa: E501
        """
        pass

    def test_accept_logout_request(self):
        """Test case for accept_logout_request

        Accept a Logout Request  # noqa: E501
        """
        pass

    def test_create_json_web_key_set(self):
        """Test case for create_json_web_key_set

        Generate a New JSON Web Key  # noqa: E501
        """
        pass

    def test_create_o_auth2_client(self):
        """Test case for create_o_auth2_client

        Create an OAuth 2.0 Client  # noqa: E501
        """
        pass

    def test_delete_json_web_key(self):
        """Test case for delete_json_web_key

        Delete a JSON Web Key  # noqa: E501
        """
        pass

    def test_delete_json_web_key_set(self):
        """Test case for delete_json_web_key_set

        Delete a JSON Web Key Set  # noqa: E501
        """
        pass

    def test_delete_o_auth2_client(self):
        """Test case for delete_o_auth2_client

        Deletes an OAuth 2.0 Client  # noqa: E501
        """
        pass

    def test_delete_o_auth2_token(self):
        """Test case for delete_o_auth2_token

        Delete OAuth2 Access Tokens from a Client  # noqa: E501
        """
        pass

    def test_delete_trusted_jwt_grant_issuer(self):
        """Test case for delete_trusted_jwt_grant_issuer

        Delete a Trusted OAuth2 JWT Bearer Grant Type Issuer  # noqa: E501
        """
        pass

    def test_flush_inactive_o_auth2_tokens(self):
        """Test case for flush_inactive_o_auth2_tokens

        Flush Expired OAuth2 Access Tokens  # noqa: E501
        """
        pass

    def test_get_consent_request(self):
        """Test case for get_consent_request

        Get Consent Request Information  # noqa: E501
        """
        pass

    def test_get_json_web_key(self):
        """Test case for get_json_web_key

        Fetch a JSON Web Key  # noqa: E501
        """
        pass

    def test_get_json_web_key_set(self):
        """Test case for get_json_web_key_set

        Retrieve a JSON Web Key Set  # noqa: E501
        """
        pass

    def test_get_login_request(self):
        """Test case for get_login_request

        Get a Login Request  # noqa: E501
        """
        pass

    def test_get_logout_request(self):
        """Test case for get_logout_request

        Get a Logout Request  # noqa: E501
        """
        pass

    def test_get_o_auth2_client(self):
        """Test case for get_o_auth2_client

        Get an OAuth 2.0 Client  # noqa: E501
        """
        pass

    def test_get_trusted_jwt_grant_issuer(self):
        """Test case for get_trusted_jwt_grant_issuer

        Get a Trusted OAuth2 JWT Bearer Grant Type Issuer  # noqa: E501
        """
        pass

    def test_introspect_o_auth2_token(self):
        """Test case for introspect_o_auth2_token

        Introspect OAuth2 Tokens  # noqa: E501
        """
        pass

    def test_list_o_auth2_clients(self):
        """Test case for list_o_auth2_clients

        List OAuth 2.0 Clients  # noqa: E501
        """
        pass

    def test_list_subject_consent_sessions(self):
        """Test case for list_subject_consent_sessions

        Lists All Consent Sessions of a Subject  # noqa: E501
        """
        pass

    def test_list_trusted_jwt_grant_issuers(self):
        """Test case for list_trusted_jwt_grant_issuers

        List Trusted OAuth2 JWT Bearer Grant Type Issuers  # noqa: E501
        """
        pass

    def test_patch_o_auth2_client(self):
        """Test case for patch_o_auth2_client

        Patch an OAuth 2.0 Client  # noqa: E501
        """
        pass

    def test_reject_consent_request(self):
        """Test case for reject_consent_request

        Reject a Consent Request  # noqa: E501
        """
        pass

    def test_reject_login_request(self):
        """Test case for reject_login_request

        Reject a Login Request  # noqa: E501
        """
        pass

    def test_reject_logout_request(self):
        """Test case for reject_logout_request

        Reject a Logout Request  # noqa: E501
        """
        pass

    def test_revoke_authentication_session(self):
        """Test case for revoke_authentication_session

        Invalidates All Login Sessions of a Certain User Invalidates a Subject's Authentication Session  # noqa: E501
        """
        pass

    def test_revoke_consent_sessions(self):
        """Test case for revoke_consent_sessions

        Revokes Consent Sessions of a Subject for a Specific OAuth 2.0 Client  # noqa: E501
        """
        pass

    def test_trust_jwt_grant_issuer(self):
        """Test case for trust_jwt_grant_issuer

        Trust an OAuth2 JWT Bearer Grant Type Issuer  # noqa: E501
        """
        pass

    def test_update_json_web_key(self):
        """Test case for update_json_web_key

        Update a JSON Web Key  # noqa: E501
        """
        pass

    def test_update_json_web_key_set(self):
        """Test case for update_json_web_key_set

        Update a JSON Web Key Set  # noqa: E501
        """
        pass

    def test_update_o_auth2_client(self):
        """Test case for update_o_auth2_client

        Update an OAuth 2.0 Client  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
