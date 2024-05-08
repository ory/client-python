# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.11.7
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.credential_supported_draft00 import CredentialSupportedDraft00

class TestCredentialSupportedDraft00(unittest.TestCase):
    """CredentialSupportedDraft00 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CredentialSupportedDraft00:
        """Test CredentialSupportedDraft00
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CredentialSupportedDraft00`
        """
        model = CredentialSupportedDraft00()
        if include_optional:
            return CredentialSupportedDraft00(
                cryptographic_binding_methods_supported = [
                    ''
                    ],
                cryptographic_suites_supported = [
                    ''
                    ],
                format = '',
                types = [
                    ''
                    ]
            )
        else:
            return CredentialSupportedDraft00(
        )
        """

    def testCredentialSupportedDraft00(self):
        """Test CredentialSupportedDraft00"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
