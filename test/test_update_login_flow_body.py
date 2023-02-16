"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.1.11
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.update_login_flow_with_lookup_secret_method import UpdateLoginFlowWithLookupSecretMethod
from ory_client.model.update_login_flow_with_oidc_method import UpdateLoginFlowWithOidcMethod
from ory_client.model.update_login_flow_with_password_method import UpdateLoginFlowWithPasswordMethod
from ory_client.model.update_login_flow_with_totp_method import UpdateLoginFlowWithTotpMethod
from ory_client.model.update_login_flow_with_web_authn_method import UpdateLoginFlowWithWebAuthnMethod
globals()['UpdateLoginFlowWithLookupSecretMethod'] = UpdateLoginFlowWithLookupSecretMethod
globals()['UpdateLoginFlowWithOidcMethod'] = UpdateLoginFlowWithOidcMethod
globals()['UpdateLoginFlowWithPasswordMethod'] = UpdateLoginFlowWithPasswordMethod
globals()['UpdateLoginFlowWithTotpMethod'] = UpdateLoginFlowWithTotpMethod
globals()['UpdateLoginFlowWithWebAuthnMethod'] = UpdateLoginFlowWithWebAuthnMethod
from ory_client.model.update_login_flow_body import UpdateLoginFlowBody


class TestUpdateLoginFlowBody(unittest.TestCase):
    """UpdateLoginFlowBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateLoginFlowBody(self):
        """Test UpdateLoginFlowBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UpdateLoginFlowBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
