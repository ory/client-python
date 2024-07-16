# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.14.0
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.identity_credentials_oidc import IdentityCredentialsOidc

class TestIdentityCredentialsOidc(unittest.TestCase):
    """IdentityCredentialsOidc unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityCredentialsOidc:
        """Test IdentityCredentialsOidc
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityCredentialsOidc`
        """
        model = IdentityCredentialsOidc()
        if include_optional:
            return IdentityCredentialsOidc(
                providers = [
                    ory_client.models.credentials_oidc_provider_is_contains_a_specific_open_id_c_onnect_credential_for_a_particular_connection_(e/g/_google)/.CredentialsOIDCProvider is contains a specific OpenID COnnect credential for a particular connection (e.g. Google).(
                        initial_access_token = '', 
                        initial_id_token = '', 
                        initial_refresh_token = '', 
                        organization = '', 
                        provider = '', 
                        subject = '', )
                    ]
            )
        else:
            return IdentityCredentialsOidc(
        )
        """

    def testIdentityCredentialsOidc(self):
        """Test IdentityCredentialsOidc"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
