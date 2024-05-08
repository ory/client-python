# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.11.7
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.check_opl_syntax_result import CheckOplSyntaxResult

class TestCheckOplSyntaxResult(unittest.TestCase):
    """CheckOplSyntaxResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckOplSyntaxResult:
        """Test CheckOplSyntaxResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckOplSyntaxResult`
        """
        model = CheckOplSyntaxResult()
        if include_optional:
            return CheckOplSyntaxResult(
                errors = [
                    ory_client.models.parse_error.ParseError(
                        end = ory_client.models.source_position.SourcePosition(
                            line = 56, 
                            column = 56, ), 
                        message = '', 
                        start = ory_client.models.source_position.SourcePosition(
                            line = 56, 
                            column = 56, ), )
                    ]
            )
        else:
            return CheckOplSyntaxResult(
        )
        """

    def testCheckOplSyntaxResult(self):
        """Test CheckOplSyntaxResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
