"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.76
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.project_revision import ProjectRevision
globals()['ProjectRevision'] = ProjectRevision
from ory_client.model.project_revisions import ProjectRevisions


class TestProjectRevisions(unittest.TestCase):
    """ProjectRevisions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProjectRevisions(self):
        """Test ProjectRevisions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProjectRevisions()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
