# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.12.2
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.parse_error import ParseError

class TestParseError(unittest.TestCase):
    """ParseError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParseError:
        """Test ParseError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParseError`
        """
        model = ParseError()
        if include_optional:
            return ParseError(
                end = ory_client.models.source_position.SourcePosition(
                    line = 56, 
                    column = 56, ),
                message = '',
                start = ory_client.models.source_position.SourcePosition(
                    line = 56, 
                    column = 56, )
            )
        else:
            return ParseError(
        )
        """

    def testParseError(self):
        """Test ParseError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
