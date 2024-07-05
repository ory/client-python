# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.1
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.accept_o_auth2_consent_request_session import AcceptOAuth2ConsentRequestSession

class TestAcceptOAuth2ConsentRequestSession(unittest.TestCase):
    """AcceptOAuth2ConsentRequestSession unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AcceptOAuth2ConsentRequestSession:
        """Test AcceptOAuth2ConsentRequestSession
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AcceptOAuth2ConsentRequestSession`
        """
        model = AcceptOAuth2ConsentRequestSession()
        if include_optional:
            return AcceptOAuth2ConsentRequestSession(
                access_token = None,
                id_token = None
            )
        else:
            return AcceptOAuth2ConsentRequestSession(
        )
        """

    def testAcceptOAuth2ConsentRequestSession(self):
        """Test AcceptOAuth2ConsentRequestSession"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
