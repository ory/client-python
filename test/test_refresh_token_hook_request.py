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
from ory_client.model.o_auth2_access_request import OAuth2AccessRequest
from ory_client.model.o_auth2_consent_session import OAuth2ConsentSession
globals()['OAuth2AccessRequest'] = OAuth2AccessRequest
globals()['OAuth2ConsentSession'] = OAuth2ConsentSession
from ory_client.model.refresh_token_hook_request import RefreshTokenHookRequest


class TestRefreshTokenHookRequest(unittest.TestCase):
    """RefreshTokenHookRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRefreshTokenHookRequest(self):
        """Test RefreshTokenHookRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RefreshTokenHookRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
