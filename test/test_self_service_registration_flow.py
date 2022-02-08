"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.77
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.identity_credentials_type import IdentityCredentialsType
from ory_client.model.ui_container import UiContainer
globals()['IdentityCredentialsType'] = IdentityCredentialsType
globals()['UiContainer'] = UiContainer
from ory_client.model.self_service_registration_flow import SelfServiceRegistrationFlow


class TestSelfServiceRegistrationFlow(unittest.TestCase):
    """SelfServiceRegistrationFlow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSelfServiceRegistrationFlow(self):
        """Test SelfServiceRegistrationFlow"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SelfServiceRegistrationFlow()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
