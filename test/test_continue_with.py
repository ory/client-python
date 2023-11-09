"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.2.17
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.continue_with_set_ory_session_token import ContinueWithSetOrySessionToken
from ory_client.model.continue_with_verification_ui import ContinueWithVerificationUi
from ory_client.model.continue_with_verification_ui_flow import ContinueWithVerificationUiFlow
globals()['ContinueWithSetOrySessionToken'] = ContinueWithSetOrySessionToken
globals()['ContinueWithVerificationUi'] = ContinueWithVerificationUi
globals()['ContinueWithVerificationUiFlow'] = ContinueWithVerificationUiFlow
from ory_client.model.continue_with import ContinueWith


class TestContinueWith(unittest.TestCase):
    """ContinueWith unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContinueWith(self):
        """Test ContinueWith"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ContinueWith()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
