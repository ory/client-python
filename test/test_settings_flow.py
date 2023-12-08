"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.4.5
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_client
from ory_client.model.continue_with import ContinueWith
from ory_client.model.identity import Identity
from ory_client.model.ui_container import UiContainer
globals()['ContinueWith'] = ContinueWith
globals()['Identity'] = Identity
globals()['UiContainer'] = UiContainer
from ory_client.model.settings_flow import SettingsFlow


class TestSettingsFlow(unittest.TestCase):
    """SettingsFlow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSettingsFlow(self):
        """Test SettingsFlow"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SettingsFlow()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
