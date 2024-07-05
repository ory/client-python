# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.2
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class SettingsFlowState(str, Enum):
    """
    show_form: No user data has been collected, or it is invalid, and thus the form should be shown. success: Indicates that the settings flow has been updated successfully with the provided data. Done will stay true when repeatedly checking. If set to true, done will revert back to false only when a flow with invalid (e.g. \"please use a valid phone number\") data was sent.
    """

    """
    allowed enum values
    """
    SHOW_FORM = 'show_form'
    SUCCESS = 'success'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SettingsFlowState from a JSON string"""
        return cls(json.loads(json_str))


