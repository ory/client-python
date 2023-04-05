"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.1.24
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.generic_usage import GenericUsage
globals()['GenericUsage'] = GenericUsage
from ory_client.model.usage import Usage


class TestUsage(unittest.TestCase):
    """Usage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsage(self):
        """Test Usage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Usage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
