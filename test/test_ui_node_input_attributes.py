# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.7
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.models.ui_node_input_attributes import UiNodeInputAttributes

class TestUiNodeInputAttributes(unittest.TestCase):
    """UiNodeInputAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UiNodeInputAttributes:
        """Test UiNodeInputAttributes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UiNodeInputAttributes`
        """
        model = UiNodeInputAttributes()
        if include_optional:
            return UiNodeInputAttributes(
                autocomplete = 'email',
                disabled = True,
                label = ory_client.models.ui_text.uiText(
                    context = ory_client.models.context.context(), 
                    id = 56, 
                    text = '', 
                    type = 'info', ),
                name = '',
                node_type = 'text',
                onclick = '',
                onload = '',
                pattern = '',
                required = True,
                type = 'text',
                value = None
            )
        else:
            return UiNodeInputAttributes(
                disabled = True,
                name = '',
                node_type = 'text',
                type = 'text',
        )
        """

    def testUiNodeInputAttributes(self):
        """Test UiNodeInputAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
