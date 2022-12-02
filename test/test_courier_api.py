"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.   # noqa: E501

    The version of the OpenAPI document: v1.0.2
    Contact: support@ory.sh
    Generated by: https://openapi-generator.tech
"""


import unittest

import ory_client
from ory_client.api.courier_api import CourierApi  # noqa: E501


class TestCourierApi(unittest.TestCase):
    """CourierApi unit test stubs"""

    def setUp(self):
        self.api = CourierApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_courier_messages(self):
        """Test case for list_courier_messages

        List Messages  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
