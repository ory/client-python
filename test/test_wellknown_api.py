# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.11.10
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.api.wellknown_api import WellknownApi


class TestWellknownApi(unittest.TestCase):
    """WellknownApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WellknownApi()

    def tearDown(self) -> None:
        pass

    def test_discover_json_web_keys(self) -> None:
        """Test case for discover_json_web_keys

        Discover Well-Known JSON Web Keys
        """
        pass


if __name__ == '__main__':
    unittest.main()
