# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.1
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.line_item_v1 import LineItemV1

class TestLineItemV1(unittest.TestCase):
    """LineItemV1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LineItemV1:
        """Test LineItemV1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LineItemV1`
        """
        model = LineItemV1()
        if include_optional:
            return LineItemV1(
                amount_in_cent = 56,
                description = '',
                items = [
                    ory_client.models.line_item_v1.LineItemV1(
                        amount_in_cent = 56, 
                        description = '', 
                        quantity = 56, 
                        title = '', 
                        unit_price = '', )
                    ],
                quantity = 56,
                title = '',
                unit_price = ''
            )
        else:
            return LineItemV1(
        )
        """

    def testLineItemV1(self):
        """Test LineItemV1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
