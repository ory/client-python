"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.89
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.project_revision import ProjectRevision
from ory_client.model.project_revisions import ProjectRevisions
from ory_client.model.string_slice_json_format import StringSliceJSONFormat
globals()['ProjectRevision'] = ProjectRevision
globals()['ProjectRevisions'] = ProjectRevisions
globals()['StringSliceJSONFormat'] = StringSliceJSONFormat
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
