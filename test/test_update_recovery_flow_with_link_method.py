# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.9
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.update_recovery_flow_with_link_method import UpdateRecoveryFlowWithLinkMethod

class TestUpdateRecoveryFlowWithLinkMethod(unittest.TestCase):
    """UpdateRecoveryFlowWithLinkMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateRecoveryFlowWithLinkMethod:
        """Test UpdateRecoveryFlowWithLinkMethod
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateRecoveryFlowWithLinkMethod`
        """
        model = UpdateRecoveryFlowWithLinkMethod()
        if include_optional:
            return UpdateRecoveryFlowWithLinkMethod(
                csrf_token = '',
                email = '',
                method = 'link',
                transient_payload = ory_client.models.transient_payload.transient_payload()
            )
        else:
            return UpdateRecoveryFlowWithLinkMethod(
                email = '',
                method = 'link',
        )
        """

    def testUpdateRecoveryFlowWithLinkMethod(self):
        """Test UpdateRecoveryFlowWithLinkMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
