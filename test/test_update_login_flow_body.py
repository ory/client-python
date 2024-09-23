# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.15.3
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.update_login_flow_body import UpdateLoginFlowBody

class TestUpdateLoginFlowBody(unittest.TestCase):
    """UpdateLoginFlowBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateLoginFlowBody:
        """Test UpdateLoginFlowBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateLoginFlowBody`
        """
        model = UpdateLoginFlowBody()
        if include_optional:
            return UpdateLoginFlowBody(
                csrf_token = '',
                identifier = '',
                method = '',
                password = '',
                password_identifier = '',
                transient_payload = ory_client.models.transient_payload.transient_payload(),
                id_token = '',
                id_token_nonce = '',
                provider = '',
                traits = ory_client.models.traits.traits(),
                upstream_parameters = ory_client.models.upstream_parameters.upstream_parameters(),
                totp_code = '',
                webauthn_login = '',
                lookup_secret = '',
                address = '',
                code = '',
                resend = '',
                passkey_login = ''
            )
        else:
            return UpdateLoginFlowBody(
                csrf_token = '',
                identifier = '',
                method = '',
                password = '',
                provider = '',
                totp_code = '',
                lookup_secret = '',
        )
        """

    def testUpdateLoginFlowBody(self):
        """Test UpdateLoginFlowBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
