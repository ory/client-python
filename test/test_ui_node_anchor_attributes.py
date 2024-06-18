# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.11.10
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.ui_node_anchor_attributes import UiNodeAnchorAttributes

class TestUiNodeAnchorAttributes(unittest.TestCase):
    """UiNodeAnchorAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UiNodeAnchorAttributes:
        """Test UiNodeAnchorAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UiNodeAnchorAttributes`
        """
        model = UiNodeAnchorAttributes()
        if include_optional:
            return UiNodeAnchorAttributes(
                href = '',
                id = '',
                node_type = 'text',
                title = ory_client.models.ui_text.uiText(
                    context = ory_client.models.context.context(), 
                    id = 56, 
                    text = '', 
                    type = 'info', )
            )
        else:
            return UiNodeAnchorAttributes(
                href = '',
                id = '',
                node_type = 'text',
                title = ory_client.models.ui_text.uiText(
                    context = ory_client.models.context.context(), 
                    id = 56, 
                    text = '', 
                    type = 'info', ),
        )
        """

    def testUiNodeAnchorAttributes(self):
        """Test UiNodeAnchorAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
