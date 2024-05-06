# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.11.6
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.reject_o_auth2_request import RejectOAuth2Request

class TestRejectOAuth2Request(unittest.TestCase):
    """RejectOAuth2Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RejectOAuth2Request:
        """Test RejectOAuth2Request
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RejectOAuth2Request`
        """
        model = RejectOAuth2Request()
        if include_optional:
            return RejectOAuth2Request(
                error = '',
                error_debug = '',
                error_description = '',
                error_hint = '',
                status_code = 56
            )
        else:
            return RejectOAuth2Request(
        )
        """

    def testRejectOAuth2Request(self):
        """Test RejectOAuth2Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
