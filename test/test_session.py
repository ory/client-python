"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.2.0-alpha.16
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.authenticator_assurance_level import AuthenticatorAssuranceLevel
from ory_client.model.identity import Identity
from ory_client.model.session_authentication_methods import SessionAuthenticationMethods
globals()['AuthenticatorAssuranceLevel'] = AuthenticatorAssuranceLevel
globals()['Identity'] = Identity
globals()['SessionAuthenticationMethods'] = SessionAuthenticationMethods
from ory_client.model.session import Session


class TestSession(unittest.TestCase):
    """Session unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSession(self):
        """Test Session"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Session()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
