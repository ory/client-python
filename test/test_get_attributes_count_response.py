# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.14.4
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.get_attributes_count_response import GetAttributesCountResponse

class TestGetAttributesCountResponse(unittest.TestCase):
    """GetAttributesCountResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAttributesCountResponse:
        """Test GetAttributesCountResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAttributesCountResponse`
        """
        model = GetAttributesCountResponse()
        if include_optional:
            return GetAttributesCountResponse(
                data = [
                    ory_client.models.attributes_count_datapoint.AttributesCountDatapoint(
                        count = 56, 
                        name = '', )
                    ]
            )
        else:
            return GetAttributesCountResponse(
                data = [
                    ory_client.models.attributes_count_datapoint.AttributesCountDatapoint(
                        count = 56, 
                        name = '', )
                    ],
        )
        """

    def testGetAttributesCountResponse(self):
        """Test GetAttributesCountResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
