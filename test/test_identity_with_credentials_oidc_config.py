"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.2.7
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.identity_with_credentials_oidc_config_provider import IdentityWithCredentialsOidcConfigProvider
from ory_client.model.identity_with_credentials_password_config import IdentityWithCredentialsPasswordConfig
globals()['IdentityWithCredentialsOidcConfigProvider'] = IdentityWithCredentialsOidcConfigProvider
globals()['IdentityWithCredentialsPasswordConfig'] = IdentityWithCredentialsPasswordConfig
from ory_client.model.identity_with_credentials_oidc_config import IdentityWithCredentialsOidcConfig


class TestIdentityWithCredentialsOidcConfig(unittest.TestCase):
    """IdentityWithCredentialsOidcConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIdentityWithCredentialsOidcConfig(self):
        """Test IdentityWithCredentialsOidcConfig"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IdentityWithCredentialsOidcConfig()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
