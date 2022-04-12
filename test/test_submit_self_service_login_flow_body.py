"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.162
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.submit_self_service_login_flow_with_lookup_secret_method_body import SubmitSelfServiceLoginFlowWithLookupSecretMethodBody
from ory_client.model.submit_self_service_login_flow_with_oidc_method_body import SubmitSelfServiceLoginFlowWithOidcMethodBody
from ory_client.model.submit_self_service_login_flow_with_password_method_body import SubmitSelfServiceLoginFlowWithPasswordMethodBody
from ory_client.model.submit_self_service_login_flow_with_totp_method_body import SubmitSelfServiceLoginFlowWithTotpMethodBody
from ory_client.model.submit_self_service_login_flow_with_web_authn_method_body import SubmitSelfServiceLoginFlowWithWebAuthnMethodBody
globals()['SubmitSelfServiceLoginFlowWithLookupSecretMethodBody'] = SubmitSelfServiceLoginFlowWithLookupSecretMethodBody
globals()['SubmitSelfServiceLoginFlowWithOidcMethodBody'] = SubmitSelfServiceLoginFlowWithOidcMethodBody
globals()['SubmitSelfServiceLoginFlowWithPasswordMethodBody'] = SubmitSelfServiceLoginFlowWithPasswordMethodBody
globals()['SubmitSelfServiceLoginFlowWithTotpMethodBody'] = SubmitSelfServiceLoginFlowWithTotpMethodBody
globals()['SubmitSelfServiceLoginFlowWithWebAuthnMethodBody'] = SubmitSelfServiceLoginFlowWithWebAuthnMethodBody
from ory_client.model.submit_self_service_login_flow_body import SubmitSelfServiceLoginFlowBody


class TestSubmitSelfServiceLoginFlowBody(unittest.TestCase):
    """SubmitSelfServiceLoginFlowBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubmitSelfServiceLoginFlowBody(self):
        """Test SubmitSelfServiceLoginFlowBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SubmitSelfServiceLoginFlowBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
