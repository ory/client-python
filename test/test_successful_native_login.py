"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.2.3
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.session import Session
globals()['Session'] = Session
from ory_client.model.successful_native_login import SuccessfulNativeLogin


class TestSuccessfulNativeLogin(unittest.TestCase):
    """SuccessfulNativeLogin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSuccessfulNativeLogin(self):
        """Test SuccessfulNativeLogin"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SuccessfulNativeLogin()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
