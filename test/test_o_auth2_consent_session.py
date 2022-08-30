"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.2.0-alpha.24
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.headers import Headers
from ory_client.model.id_token_claims import IDTokenClaims
from ory_client.model.o_auth2_consent_session_expires_at import OAuth2ConsentSessionExpiresAt
globals()['Headers'] = Headers
globals()['IDTokenClaims'] = IDTokenClaims
globals()['OAuth2ConsentSessionExpiresAt'] = OAuth2ConsentSessionExpiresAt
from ory_client.model.o_auth2_consent_session import OAuth2ConsentSession


class TestOAuth2ConsentSession(unittest.TestCase):
    """OAuth2ConsentSession unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOAuth2ConsentSession(self):
        """Test OAuth2ConsentSession"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OAuth2ConsentSession()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
