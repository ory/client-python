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

from ory_client.api.relationship_api import RelationshipApi


class TestRelationshipApi(unittest.TestCase):
    """RelationshipApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RelationshipApi()

    def tearDown(self) -> None:
        pass

    def test_check_opl_syntax(self) -> None:
        """Test case for check_opl_syntax

        Check the syntax of an OPL file
        """
        pass

    def test_create_relationship(self) -> None:
        """Test case for create_relationship

        Create a Relationship
        """
        pass

    def test_delete_relationships(self) -> None:
        """Test case for delete_relationships

        Delete Relationships
        """
        pass

    def test_get_relationships(self) -> None:
        """Test case for get_relationships

        Query relationships
        """
        pass

    def test_list_relationship_namespaces(self) -> None:
        """Test case for list_relationship_namespaces

        Query namespaces
        """
        pass

    def test_patch_relationships(self) -> None:
        """Test case for patch_relationships

        Patch Multiple Relationships
        """
        pass


if __name__ == '__main__':
    unittest.main()
