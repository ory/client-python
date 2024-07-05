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

from ory_client.models.normalized_project_revision_hook import NormalizedProjectRevisionHook

class TestNormalizedProjectRevisionHook(unittest.TestCase):
    """NormalizedProjectRevisionHook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NormalizedProjectRevisionHook:
        """Test NormalizedProjectRevisionHook
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NormalizedProjectRevisionHook`
        """
        model = NormalizedProjectRevisionHook()
        if include_optional:
            return NormalizedProjectRevisionHook(
                config_key = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                hook = '',
                id = '',
                project_revision_id = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                web_hook_config_auth_api_key_in = 'header',
                web_hook_config_auth_api_key_name = 'X-API-Key',
                web_hook_config_auth_api_key_value = 'eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ',
                web_hook_config_auth_basic_auth_password = '',
                web_hook_config_auth_basic_auth_user = '',
                web_hook_config_auth_type = '',
                web_hook_config_body = 'base64://ZnVuY3Rpb24oY3R4KSB7CiAgaWRlbnRpdHlfaWQ6IGlmIGN0eFsiaWRlbnRpdHkiXSAhPSBudWxsIHRoZW4gY3R4LmlkZW50aXR5LmlkLAp9=',
                web_hook_config_can_interrupt = True,
                web_hook_config_method = 'POST',
                web_hook_config_response_ignore = True,
                web_hook_config_response_parse = True,
                web_hook_config_url = 'https://www.example.org/web-hook-listener'
            )
        else:
            return NormalizedProjectRevisionHook(
                config_key = '',
                hook = '',
        )
        """

    def testNormalizedProjectRevisionHook(self):
        """Test NormalizedProjectRevisionHook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
