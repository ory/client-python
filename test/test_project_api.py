# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.7
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.api.project_api import ProjectApi


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectApi()

    def tearDown(self) -> None:
        pass

    def test_create_organization(self) -> None:
        """Test case for create_organization

        """
        pass

    def test_create_project(self) -> None:
        """Test case for create_project

        Create a Project
        """
        pass

    def test_create_project_api_key(self) -> None:
        """Test case for create_project_api_key

        Create project API token
        """
        pass

    def test_delete_organization(self) -> None:
        """Test case for delete_organization

        """
        pass

    def test_delete_project_api_key(self) -> None:
        """Test case for delete_project_api_key

        Delete project API token
        """
        pass

    def test_get_organization(self) -> None:
        """Test case for get_organization

        Returns a B2B SSO Organization for a project by its ID
        """
        pass

    def test_get_project(self) -> None:
        """Test case for get_project

        Get a Project
        """
        pass

    def test_get_project_members(self) -> None:
        """Test case for get_project_members

        Get all members associated with this project
        """
        pass

    def test_list_organizations(self) -> None:
        """Test case for list_organizations

        """
        pass

    def test_list_project_api_keys(self) -> None:
        """Test case for list_project_api_keys

        List a project's API Tokens
        """
        pass

    def test_list_projects(self) -> None:
        """Test case for list_projects

        List All Projects
        """
        pass

    def test_patch_project(self) -> None:
        """Test case for patch_project

        Patch an Ory Network Project Configuration
        """
        pass

    def test_purge_project(self) -> None:
        """Test case for purge_project

        Irrecoverably purge a project
        """
        pass

    def test_remove_project_member(self) -> None:
        """Test case for remove_project_member

        Remove a member associated with this project
        """
        pass

    def test_set_project(self) -> None:
        """Test case for set_project

        Update an Ory Network Project Configuration
        """
        pass

    def test_update_organization(self) -> None:
        """Test case for update_organization

        """
        pass


if __name__ == '__main__':
    unittest.main()
