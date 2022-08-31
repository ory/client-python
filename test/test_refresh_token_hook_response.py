"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.2.0-alpha.25
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.accept_o_auth2_consent_request_session import AcceptOAuth2ConsentRequestSession
globals()['AcceptOAuth2ConsentRequestSession'] = AcceptOAuth2ConsentRequestSession
from ory_client.model.refresh_token_hook_response import RefreshTokenHookResponse


class TestRefreshTokenHookResponse(unittest.TestCase):
    """RefreshTokenHookResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRefreshTokenHookResponse(self):
        """Test RefreshTokenHookResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RefreshTokenHookResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
