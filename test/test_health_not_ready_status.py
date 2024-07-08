# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.6
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.health_not_ready_status import HealthNotReadyStatus

class TestHealthNotReadyStatus(unittest.TestCase):
    """HealthNotReadyStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HealthNotReadyStatus:
        """Test HealthNotReadyStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HealthNotReadyStatus`
        """
        model = HealthNotReadyStatus()
        if include_optional:
            return HealthNotReadyStatus(
                errors = {
                    'key' : ''
                    }
            )
        else:
            return HealthNotReadyStatus(
        )
        """

    def testHealthNotReadyStatus(self):
        """Test HealthNotReadyStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
