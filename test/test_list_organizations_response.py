"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.8.0
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.organization import Organization
globals()['Organization'] = Organization
from ory_client.model.list_organizations_response import ListOrganizationsResponse


class TestListOrganizationsResponse(unittest.TestCase):
    """ListOrganizationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListOrganizationsResponse(self):
        """Test ListOrganizationsResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListOrganizationsResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
