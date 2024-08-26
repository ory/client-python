# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.14.4
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_client.api.events_api import EventsApi


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EventsApi()

    def tearDown(self) -> None:
        pass

    def test_create_event_stream(self) -> None:
        """Test case for create_event_stream

        Create an event stream for your project.
        """
        pass

    def test_delete_event_stream(self) -> None:
        """Test case for delete_event_stream

        Remove an event stream from a project
        """
        pass

    def test_list_event_streams(self) -> None:
        """Test case for list_event_streams

        List all event streams for the project. This endpoint is not paginated.
        """
        pass

    def test_set_event_stream(self) -> None:
        """Test case for set_event_stream

        Update an event stream for a project.
        """
        pass


if __name__ == '__main__':
    unittest.main()
