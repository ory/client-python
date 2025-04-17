# coding: utf-8

"""
    Ory APIs

    # Introduction Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.  ## SDKs This document describes the APIs available in the Ory Network. The APIs are available as SDKs for the following languages:  | Language       | Download SDK                                                     | Documentation                                                                        | | -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ | | Dart           | [pub.dev](https://pub.dev/packages/ory_client)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/dart/README.md)       | | .NET           | [nuget.org](https://www.nuget.org/packages/Ory.Client/)          | [README](https://github.com/ory/sdk/blob/master/clients/client/dotnet/README.md)     | | Elixir         | [hex.pm](https://hex.pm/packages/ory_client)                     | [README](https://github.com/ory/sdk/blob/master/clients/client/elixir/README.md)     | | Go             | [github.com](https://github.com/ory/client-go)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/go/README.md)         | | Java           | [maven.org](https://search.maven.org/artifact/sh.ory/ory-client) | [README](https://github.com/ory/sdk/blob/master/clients/client/java/README.md)       | | JavaScript     | [npmjs.com](https://www.npmjs.com/package/@ory/client)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript/README.md) | | JavaScript (With fetch) | [npmjs.com](https://www.npmjs.com/package/@ory/client-fetch)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript-fetch/README.md) |  | PHP            | [packagist.org](https://packagist.org/packages/ory/client)       | [README](https://github.com/ory/sdk/blob/master/clients/client/php/README.md)        | | Python         | [pypi.org](https://pypi.org/project/ory-client/)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/python/README.md)     | | Ruby           | [rubygems.org](https://rubygems.org/gems/ory-client)             | [README](https://github.com/ory/sdk/blob/master/clients/client/ruby/README.md)       | | Rust           | [crates.io](https://crates.io/crates/ory-client)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/rust/README.md)       | 

    The version of the OpenAPI document: v1.20.7
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

        Create an Enterprise SSO Organization
        """
        pass

    def test_create_project(self) -> None:
        """Test case for create_project

        Create a Project
        """
        pass

    def test_create_project_api_key(self) -> None:
        """Test case for create_project_api_key

        Create project API key
        """
        pass

    def test_delete_organization(self) -> None:
        """Test case for delete_organization

        Delete Enterprise SSO Organization
        """
        pass

    def test_delete_project_api_key(self) -> None:
        """Test case for delete_project_api_key

        Delete project API key
        """
        pass

    def test_get_organization(self) -> None:
        """Test case for get_organization

        Get Enterprise SSO Organization by ID
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

        List all Enterprise SSO organizations
        """
        pass

    def test_list_project_api_keys(self) -> None:
        """Test case for list_project_api_keys

        List a project's API keys
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

    def test_patch_project_with_revision(self) -> None:
        """Test case for patch_project_with_revision

        Patch an Ory Network Project Configuration based on a revision ID
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

        Update an Enterprise SSO Organization
        """
        pass


if __name__ == '__main__':
    unittest.main()
