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

from ory_client.models.error_generic import ErrorGeneric

class TestErrorGeneric(unittest.TestCase):
    """ErrorGeneric unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorGeneric:
        """Test ErrorGeneric
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorGeneric`
        """
        model = ErrorGeneric()
        if include_optional:
            return ErrorGeneric(
                error = ory_client.models.generic_error_content.genericErrorContent(
                    debug = 'The database adapter was unable to find the element', 
                    error_description = 'Object with ID 12345 does not exist', 
                    message = '', 
                    status_code = 404, )
            )
        else:
            return ErrorGeneric(
                error = ory_client.models.generic_error_content.genericErrorContent(
                    debug = 'The database adapter was unable to find the element', 
                    error_description = 'Object with ID 12345 does not exist', 
                    message = '', 
                    status_code = 404, ),
        )
        """

    def testErrorGeneric(self):
        """Test ErrorGeneric"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
