"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.2.0-alpha.60
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_client
from ory_client.api.namespaces_api import NamespacesApi  # noqa: E501


class TestNamespacesApi(unittest.TestCase):
    """NamespacesApi unit test stubs"""

    def setUp(self):
        self.api = NamespacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_namespaces(self):
        """Test case for get_namespaces

        Query namespaces  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
