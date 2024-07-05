# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.1
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.api.o_auth2_api import OAuth2Api


class TestOAuth2Api(unittest.TestCase):
    """OAuth2Api unit test stubs"""

    def setUp(self) -> None:
        self.api = OAuth2Api()

    def tearDown(self) -> None:
        pass

    def test_accept_o_auth2_consent_request(self) -> None:
        """Test case for accept_o_auth2_consent_request

        Accept OAuth 2.0 Consent Request
        """
        pass

    def test_accept_o_auth2_login_request(self) -> None:
        """Test case for accept_o_auth2_login_request

        Accept OAuth 2.0 Login Request
        """
        pass

    def test_accept_o_auth2_logout_request(self) -> None:
        """Test case for accept_o_auth2_logout_request

        Accept OAuth 2.0 Session Logout Request
        """
        pass

    def test_create_o_auth2_client(self) -> None:
        """Test case for create_o_auth2_client

        Create OAuth 2.0 Client
        """
        pass

    def test_delete_o_auth2_client(self) -> None:
        """Test case for delete_o_auth2_client

        Delete OAuth 2.0 Client
        """
        pass

    def test_delete_o_auth2_token(self) -> None:
        """Test case for delete_o_auth2_token

        Delete OAuth 2.0 Access Tokens from specific OAuth 2.0 Client
        """
        pass

    def test_delete_trusted_o_auth2_jwt_grant_issuer(self) -> None:
        """Test case for delete_trusted_o_auth2_jwt_grant_issuer

        Delete Trusted OAuth2 JWT Bearer Grant Type Issuer
        """
        pass

    def test_get_o_auth2_client(self) -> None:
        """Test case for get_o_auth2_client

        Get an OAuth 2.0 Client
        """
        pass

    def test_get_o_auth2_consent_request(self) -> None:
        """Test case for get_o_auth2_consent_request

        Get OAuth 2.0 Consent Request
        """
        pass

    def test_get_o_auth2_login_request(self) -> None:
        """Test case for get_o_auth2_login_request

        Get OAuth 2.0 Login Request
        """
        pass

    def test_get_o_auth2_logout_request(self) -> None:
        """Test case for get_o_auth2_logout_request

        Get OAuth 2.0 Session Logout Request
        """
        pass

    def test_get_trusted_o_auth2_jwt_grant_issuer(self) -> None:
        """Test case for get_trusted_o_auth2_jwt_grant_issuer

        Get Trusted OAuth2 JWT Bearer Grant Type Issuer
        """
        pass

    def test_introspect_o_auth2_token(self) -> None:
        """Test case for introspect_o_auth2_token

        Introspect OAuth2 Access and Refresh Tokens
        """
        pass

    def test_list_o_auth2_clients(self) -> None:
        """Test case for list_o_auth2_clients

        List OAuth 2.0 Clients
        """
        pass

    def test_list_o_auth2_consent_sessions(self) -> None:
        """Test case for list_o_auth2_consent_sessions

        List OAuth 2.0 Consent Sessions of a Subject
        """
        pass

    def test_list_trusted_o_auth2_jwt_grant_issuers(self) -> None:
        """Test case for list_trusted_o_auth2_jwt_grant_issuers

        List Trusted OAuth2 JWT Bearer Grant Type Issuers
        """
        pass

    def test_o_auth2_authorize(self) -> None:
        """Test case for o_auth2_authorize

        OAuth 2.0 Authorize Endpoint
        """
        pass

    def test_oauth2_token_exchange(self) -> None:
        """Test case for oauth2_token_exchange

        The OAuth 2.0 Token Endpoint
        """
        pass

    def test_patch_o_auth2_client(self) -> None:
        """Test case for patch_o_auth2_client

        Patch OAuth 2.0 Client
        """
        pass

    def test_reject_o_auth2_consent_request(self) -> None:
        """Test case for reject_o_auth2_consent_request

        Reject OAuth 2.0 Consent Request
        """
        pass

    def test_reject_o_auth2_login_request(self) -> None:
        """Test case for reject_o_auth2_login_request

        Reject OAuth 2.0 Login Request
        """
        pass

    def test_reject_o_auth2_logout_request(self) -> None:
        """Test case for reject_o_auth2_logout_request

        Reject OAuth 2.0 Session Logout Request
        """
        pass

    def test_revoke_o_auth2_consent_sessions(self) -> None:
        """Test case for revoke_o_auth2_consent_sessions

        Revoke OAuth 2.0 Consent Sessions of a Subject
        """
        pass

    def test_revoke_o_auth2_login_sessions(self) -> None:
        """Test case for revoke_o_auth2_login_sessions

        Revokes OAuth 2.0 Login Sessions by either a Subject or a SessionID
        """
        pass

    def test_revoke_o_auth2_token(self) -> None:
        """Test case for revoke_o_auth2_token

        Revoke OAuth 2.0 Access or Refresh Token
        """
        pass

    def test_set_o_auth2_client(self) -> None:
        """Test case for set_o_auth2_client

        Set OAuth 2.0 Client
        """
        pass

    def test_set_o_auth2_client_lifespans(self) -> None:
        """Test case for set_o_auth2_client_lifespans

        Set OAuth2 Client Token Lifespans
        """
        pass

    def test_trust_o_auth2_jwt_grant_issuer(self) -> None:
        """Test case for trust_o_auth2_jwt_grant_issuer

        Trust OAuth2 JWT Bearer Grant Type Issuer
        """
        pass


if __name__ == '__main__':
    unittest.main()
