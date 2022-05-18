"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v0.0.1-alpha.178
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.ui_node_anchor_attributes import UiNodeAnchorAttributes
from ory_client.model.ui_node_image_attributes import UiNodeImageAttributes
from ory_client.model.ui_node_input_attributes import UiNodeInputAttributes
from ory_client.model.ui_node_script_attributes import UiNodeScriptAttributes
from ory_client.model.ui_node_text_attributes import UiNodeTextAttributes
from ory_client.model.ui_text import UiText
globals()['UiNodeAnchorAttributes'] = UiNodeAnchorAttributes
globals()['UiNodeImageAttributes'] = UiNodeImageAttributes
globals()['UiNodeInputAttributes'] = UiNodeInputAttributes
globals()['UiNodeScriptAttributes'] = UiNodeScriptAttributes
globals()['UiNodeTextAttributes'] = UiNodeTextAttributes
globals()['UiText'] = UiText
from ory_client.model.ui_node_attributes import UiNodeAttributes


class TestUiNodeAttributes(unittest.TestCase):
    """UiNodeAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUiNodeAttributes(self):
        """Test UiNodeAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UiNodeAttributes()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
