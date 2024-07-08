# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.9
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.o_auth2_client import OAuth2Client

class TestOAuth2Client(unittest.TestCase):
    """OAuth2Client unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuth2Client:
        """Test OAuth2Client
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuth2Client`
        """
        model = OAuth2Client()
        if include_optional:
            return OAuth2Client(
                access_token_strategy = '',
                allowed_cors_origins = [
                    ''
                    ],
                audience = [
                    ''
                    ],
                authorization_code_grant_access_token_lifespan = '4ms',
                authorization_code_grant_id_token_lifespan = '4ms',
                authorization_code_grant_refresh_token_lifespan = '4ms',
                backchannel_logout_session_required = True,
                backchannel_logout_uri = '',
                client_credentials_grant_access_token_lifespan = '4ms',
                client_id = '',
                client_name = '',
                client_secret = '',
                client_secret_expires_at = 56,
                client_uri = '',
                contacts = [
                    ''
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                frontchannel_logout_session_required = True,
                frontchannel_logout_uri = '',
                grant_types = [
                    ''
                    ],
                implicit_grant_access_token_lifespan = '4ms',
                implicit_grant_id_token_lifespan = '4ms',
                jwks = None,
                jwks_uri = '',
                jwt_bearer_grant_access_token_lifespan = '4ms',
                logo_uri = '',
                metadata = ory_client.models.json_raw_message_represents_a_json/raw_message_that_works_well_with_json,_sql,_and_swagger/.JSONRawMessage represents a json.RawMessage that works well with JSON, SQL, and Swagger.(),
                owner = '',
                policy_uri = '',
                post_logout_redirect_uris = [
                    ''
                    ],
                redirect_uris = [
                    ''
                    ],
                refresh_token_grant_access_token_lifespan = '4ms',
                refresh_token_grant_id_token_lifespan = '4ms',
                refresh_token_grant_refresh_token_lifespan = '4ms',
                registration_access_token = '',
                registration_client_uri = '',
                request_object_signing_alg = '',
                request_uris = [
                    ''
                    ],
                response_types = [
                    ''
                    ],
                scope = 'scope1 scope-2 scope.3 scope:4',
                sector_identifier_uri = '',
                skip_consent = True,
                skip_logout_consent = True,
                subject_type = '',
                token_endpoint_auth_method = 'client_secret_basic',
                token_endpoint_auth_signing_alg = '',
                tos_uri = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                userinfo_signed_response_alg = ''
            )
        else:
            return OAuth2Client(
        )
        """

    def testOAuth2Client(self):
        """Test OAuth2Client"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
