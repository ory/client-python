"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.51
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_client
from ory_client.api.v0alpha0_api import V0alpha0Api  # noqa: E501


class TestV0alpha0Api(unittest.TestCase):
    """V0alpha0Api unit test stubs"""

    def setUp(self):
        self.api = V0alpha0Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project(self):
        """Test case for create_project

        Create a Project  # noqa: E501
        """
        pass

    def test_get_project(self):
        """Test case for get_project

        Get a Project  # noqa: E501
        """
        pass

    def test_list_projects(self):
        """Test case for list_projects

        List All Projects  # noqa: E501
        """
        pass

    def test_update_project(self):
        """Test case for update_project

        Update a Project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
