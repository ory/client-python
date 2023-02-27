"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.1.21
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_client
from ory_client.api.identity_api import IdentityApi  # noqa: E501


class TestIdentityApi(unittest.TestCase):
    """IdentityApi unit test stubs"""

    def setUp(self):
        self.api = IdentityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_identity(self):
        """Test case for create_identity

        Create an Identity  # noqa: E501
        """
        pass

    def test_create_recovery_code_for_identity(self):
        """Test case for create_recovery_code_for_identity

        Create a Recovery Code  # noqa: E501
        """
        pass

    def test_create_recovery_link_for_identity(self):
        """Test case for create_recovery_link_for_identity

        Create a Recovery Link  # noqa: E501
        """
        pass

    def test_delete_identity(self):
        """Test case for delete_identity

        Delete an Identity  # noqa: E501
        """
        pass

    def test_delete_identity_credentials(self):
        """Test case for delete_identity_credentials

        Delete a credential for a specific identity  # noqa: E501
        """
        pass

    def test_delete_identity_sessions(self):
        """Test case for delete_identity_sessions

        Delete & Invalidate an Identity's Sessions  # noqa: E501
        """
        pass

    def test_disable_session(self):
        """Test case for disable_session

        Deactivate a Session  # noqa: E501
        """
        pass

    def test_extend_session(self):
        """Test case for extend_session

        Extend a Session  # noqa: E501
        """
        pass

    def test_get_identity(self):
        """Test case for get_identity

        Get an Identity  # noqa: E501
        """
        pass

    def test_get_identity_schema(self):
        """Test case for get_identity_schema

        Get Identity JSON Schema  # noqa: E501
        """
        pass

    def test_get_session(self):
        """Test case for get_session

        Get Session  # noqa: E501
        """
        pass

    def test_list_identities(self):
        """Test case for list_identities

        List Identities  # noqa: E501
        """
        pass

    def test_list_identity_schemas(self):
        """Test case for list_identity_schemas

        Get all Identity Schemas  # noqa: E501
        """
        pass

    def test_list_identity_sessions(self):
        """Test case for list_identity_sessions

        List an Identity's Sessions  # noqa: E501
        """
        pass

    def test_list_sessions(self):
        """Test case for list_sessions

        List All Sessions  # noqa: E501
        """
        pass

    def test_patch_identity(self):
        """Test case for patch_identity

        Patch an Identity  # noqa: E501
        """
        pass

    def test_update_identity(self):
        """Test case for update_identity

        Update an Identity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
