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

from ory_client.models.usage import Usage

class TestUsage(unittest.TestCase):
    """Usage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Usage:
        """Test Usage
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Usage`
        """
        model = Usage()
        if include_optional:
            return Usage(
                generic_usage = ory_client.models.generic_usage_is_the_generic_usage_type_that_can_be_used_for_any_feature/.GenericUsage is the generic usage type that can be used for any feature.(
                    additional_price = ory_client.models.money.Money(
                        cents = 56, 
                        string = '', 
                        unit = '', ), 
                    included_usage = 56, )
            )
        else:
            return Usage(
        )
        """

    def testUsage(self):
        """Test Usage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
