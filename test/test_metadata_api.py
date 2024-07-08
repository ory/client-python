# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.7
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.api.metadata_api import MetadataApi


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MetadataApi()

    def tearDown(self) -> None:
        pass

    def test_get_version(self) -> None:
        """Test case for get_version

        Return Running Software Version.
        """
        pass


if __name__ == '__main__':
    unittest.main()
