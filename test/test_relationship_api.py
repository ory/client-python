"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.2.7
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_client
from ory_client.api.relationship_api import RelationshipApi  # noqa: E501


class TestRelationshipApi(unittest.TestCase):
    """RelationshipApi unit test stubs"""

    def setUp(self):
        self.api = RelationshipApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_opl_syntax(self):
        """Test case for check_opl_syntax

        Check the syntax of an OPL file  # noqa: E501
        """
        pass

    def test_create_relationship(self):
        """Test case for create_relationship

        Create a Relationship  # noqa: E501
        """
        pass

    def test_delete_relationships(self):
        """Test case for delete_relationships

        Delete Relationships  # noqa: E501
        """
        pass

    def test_get_relationships(self):
        """Test case for get_relationships

        Query relationships  # noqa: E501
        """
        pass

    def test_list_relationship_namespaces(self):
        """Test case for list_relationship_namespaces

        Query namespaces  # noqa: E501
        """
        pass

    def test_patch_relationships(self):
        """Test case for patch_relationships

        Patch Multiple Relationships  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
