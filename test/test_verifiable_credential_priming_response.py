# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.12.1
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.verifiable_credential_priming_response import VerifiableCredentialPrimingResponse

class TestVerifiableCredentialPrimingResponse(unittest.TestCase):
    """VerifiableCredentialPrimingResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VerifiableCredentialPrimingResponse:
        """Test VerifiableCredentialPrimingResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VerifiableCredentialPrimingResponse`
        """
        model = VerifiableCredentialPrimingResponse()
        if include_optional:
            return VerifiableCredentialPrimingResponse(
                c_nonce = '',
                c_nonce_expires_in = 56,
                error = '',
                error_debug = '',
                error_description = '',
                error_hint = '',
                format = '',
                status_code = 56
            )
        else:
            return VerifiableCredentialPrimingResponse(
        )
        """

    def testVerifiableCredentialPrimingResponse(self):
        """Test VerifiableCredentialPrimingResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
