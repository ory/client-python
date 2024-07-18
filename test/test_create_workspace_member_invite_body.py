# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.14.2
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.create_workspace_member_invite_body import CreateWorkspaceMemberInviteBody

class TestCreateWorkspaceMemberInviteBody(unittest.TestCase):
    """CreateWorkspaceMemberInviteBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateWorkspaceMemberInviteBody:
        """Test CreateWorkspaceMemberInviteBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateWorkspaceMemberInviteBody`
        """
        model = CreateWorkspaceMemberInviteBody()
        if include_optional:
            return CreateWorkspaceMemberInviteBody(
                invitee_email = '',
                role = 'owner'
            )
        else:
            return CreateWorkspaceMemberInviteBody(
                invitee_email = '',
                role = 'owner',
        )
        """

    def testCreateWorkspaceMemberInviteBody(self):
        """Test CreateWorkspaceMemberInviteBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
