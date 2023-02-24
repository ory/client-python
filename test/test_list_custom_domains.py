"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.1.19
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.custom_domain import CustomDomain
globals()['CustomDomain'] = CustomDomain
from ory_client.model.list_custom_domains import ListCustomDomains


class TestListCustomDomains(unittest.TestCase):
    """ListCustomDomains unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListCustomDomains(self):
        """Test ListCustomDomains"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListCustomDomains()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
