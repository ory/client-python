"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.2.0-alpha.44
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.string_slice_pipe_delimiter import StringSlicePipeDelimiter
globals()['StringSlicePipeDelimiter'] = StringSlicePipeDelimiter
from ory_client.model.o_auth2_client import OAuth2Client


class TestOAuth2Client(unittest.TestCase):
    """OAuth2Client unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOAuth2Client(self):
        """Test OAuth2Client"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OAuth2Client()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
