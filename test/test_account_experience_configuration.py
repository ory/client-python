# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.11.10
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.account_experience_configuration import AccountExperienceConfiguration

class TestAccountExperienceConfiguration(unittest.TestCase):
    """AccountExperienceConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountExperienceConfiguration:
        """Test AccountExperienceConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountExperienceConfiguration`
        """
        model = AccountExperienceConfiguration()
        if include_optional:
            return AccountExperienceConfiguration(
                account_experience_theme_stylesheet = '',
                kratos_selfservice_flows_recovery_enabled = True,
                kratos_selfservice_flows_registration_enabled = True,
                kratos_selfservice_flows_verification_enabled = True,
                organization_map = {
                    'key' : ''
                    }
            )
        else:
            return AccountExperienceConfiguration(
        )
        """

    def testAccountExperienceConfiguration(self):
        """Test AccountExperienceConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
