# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.11.6
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.o_auth2_consent_request_open_id_connect_context import OAuth2ConsentRequestOpenIDConnectContext

class TestOAuth2ConsentRequestOpenIDConnectContext(unittest.TestCase):
    """OAuth2ConsentRequestOpenIDConnectContext unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuth2ConsentRequestOpenIDConnectContext:
        """Test OAuth2ConsentRequestOpenIDConnectContext
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuth2ConsentRequestOpenIDConnectContext`
        """
        model = OAuth2ConsentRequestOpenIDConnectContext()
        if include_optional:
            return OAuth2ConsentRequestOpenIDConnectContext(
                acr_values = [
                    ''
                    ],
                display = '',
                id_token_hint_claims = {
                    'key' : null
                    },
                login_hint = '',
                ui_locales = [
                    ''
                    ]
            )
        else:
            return OAuth2ConsentRequestOpenIDConnectContext(
        )
        """

    def testOAuth2ConsentRequestOpenIDConnectContext(self):
        """Test OAuth2ConsentRequestOpenIDConnectContext"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
