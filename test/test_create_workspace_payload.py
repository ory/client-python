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

from ory_client.models.create_workspace_payload import CreateWorkspacePayload

class TestCreateWorkspacePayload(unittest.TestCase):
    """CreateWorkspacePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateWorkspacePayload:
        """Test CreateWorkspacePayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateWorkspacePayload`
        """
        model = CreateWorkspacePayload()
        if include_optional:
            return CreateWorkspacePayload(
                name = ''
            )
        else:
            return CreateWorkspacePayload(
                name = '',
        )
        """

    def testCreateWorkspacePayload(self):
        """Test CreateWorkspacePayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
