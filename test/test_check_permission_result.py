# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.9
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.check_permission_result import CheckPermissionResult

class TestCheckPermissionResult(unittest.TestCase):
    """CheckPermissionResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckPermissionResult:
        """Test CheckPermissionResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckPermissionResult`
        """
        model = CheckPermissionResult()
        if include_optional:
            return CheckPermissionResult(
                allowed = True
            )
        else:
            return CheckPermissionResult(
                allowed = True,
        )
        """

    def testCheckPermissionResult(self):
        """Test CheckPermissionResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
