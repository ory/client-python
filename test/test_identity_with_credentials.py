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

from ory_client.models.identity_with_credentials import IdentityWithCredentials

class TestIdentityWithCredentials(unittest.TestCase):
    """IdentityWithCredentials unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityWithCredentials:
        """Test IdentityWithCredentials
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityWithCredentials`
        """
        model = IdentityWithCredentials()
        if include_optional:
            return IdentityWithCredentials(
                oidc = ory_client.models.identity_with_credentials_oidc.identityWithCredentialsOidc(
                    config = ory_client.models.identity_with_credentials_oidc_config.identityWithCredentialsOidcConfig(
                        providers = [
                            ory_client.models.identity_with_credentials_oidc_config_provider.identityWithCredentialsOidcConfigProvider(
                                provider = '', 
                                subject = '', )
                            ], ), ),
                password = ory_client.models.identity_with_credentials_password.identityWithCredentialsPassword(
                    config = ory_client.models.identity_with_credentials_password_config.identityWithCredentialsPasswordConfig(
                        hashed_password = '', ), )
            )
        else:
            return IdentityWithCredentials(
        )
        """

    def testIdentityWithCredentials(self):
        """Test IdentityWithCredentials"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
