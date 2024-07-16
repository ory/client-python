# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.14.0
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.rfc6749_error_json import RFC6749ErrorJson

class TestRFC6749ErrorJson(unittest.TestCase):
    """RFC6749ErrorJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RFC6749ErrorJson:
        """Test RFC6749ErrorJson
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RFC6749ErrorJson`
        """
        model = RFC6749ErrorJson()
        if include_optional:
            return RFC6749ErrorJson(
                error = '',
                error_debug = '',
                error_description = '',
                error_hint = '',
                status_code = 56
            )
        else:
            return RFC6749ErrorJson(
        )
        """

    def testRFC6749ErrorJson(self):
        """Test RFC6749ErrorJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
