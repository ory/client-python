"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.139
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.project_services import ProjectServices
globals()['ProjectServices'] = ProjectServices
from ory_client.model.project import Project


class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProject(self):
        """Test Project"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Project()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
