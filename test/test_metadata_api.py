"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.0.0-alpha.0
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_client
from ory_client.api.metadata_api import MetadataApi  # noqa: E501


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_version(self):
        """Test case for get_version

        Return Running Software Version.  # noqa: E501
        """
        pass

    def test_is_alive(self):
        """Test case for is_alive

        Check HTTP Server Status  # noqa: E501
        """
        pass

    def test_is_ready(self):
        """Test case for is_ready

        Check HTTP Server and Database Status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
