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

from ory_client.api.identity_api import IdentityApi


class TestIdentityApi(unittest.TestCase):
    """IdentityApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IdentityApi()

    def tearDown(self) -> None:
        pass

    def test_batch_patch_identities(self) -> None:
        """Test case for batch_patch_identities

        Create multiple identities
        """
        pass

    def test_create_identity(self) -> None:
        """Test case for create_identity

        Create an Identity
        """
        pass

    def test_create_recovery_code_for_identity(self) -> None:
        """Test case for create_recovery_code_for_identity

        Create a Recovery Code
        """
        pass

    def test_create_recovery_link_for_identity(self) -> None:
        """Test case for create_recovery_link_for_identity

        Create a Recovery Link
        """
        pass

    def test_delete_identity(self) -> None:
        """Test case for delete_identity

        Delete an Identity
        """
        pass

    def test_delete_identity_credentials(self) -> None:
        """Test case for delete_identity_credentials

        Delete a credential for a specific identity
        """
        pass

    def test_delete_identity_sessions(self) -> None:
        """Test case for delete_identity_sessions

        Delete & Invalidate an Identity's Sessions
        """
        pass

    def test_disable_session(self) -> None:
        """Test case for disable_session

        Deactivate a Session
        """
        pass

    def test_extend_session(self) -> None:
        """Test case for extend_session

        Extend a Session
        """
        pass

    def test_get_identity(self) -> None:
        """Test case for get_identity

        Get an Identity
        """
        pass

    def test_get_identity_schema(self) -> None:
        """Test case for get_identity_schema

        Get Identity JSON Schema
        """
        pass

    def test_get_session(self) -> None:
        """Test case for get_session

        Get Session
        """
        pass

    def test_list_identities(self) -> None:
        """Test case for list_identities

        List Identities
        """
        pass

    def test_list_identity_schemas(self) -> None:
        """Test case for list_identity_schemas

        Get all Identity Schemas
        """
        pass

    def test_list_identity_sessions(self) -> None:
        """Test case for list_identity_sessions

        List an Identity's Sessions
        """
        pass

    def test_list_sessions(self) -> None:
        """Test case for list_sessions

        List All Sessions
        """
        pass

    def test_patch_identity(self) -> None:
        """Test case for patch_identity

        Patch an Identity
        """
        pass

    def test_update_identity(self) -> None:
        """Test case for update_identity

        Update an Identity
        """
        pass


if __name__ == '__main__':
    unittest.main()
