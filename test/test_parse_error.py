"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.2.11
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.source_position import SourcePosition
globals()['SourcePosition'] = SourcePosition
from ory_client.model.parse_error import ParseError


class TestParseError(unittest.TestCase):
    """ParseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testParseError(self):
        """Test ParseError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ParseError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
