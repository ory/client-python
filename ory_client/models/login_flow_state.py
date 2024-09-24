# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.15.4
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class LoginFlowState(str, Enum):
    """
    The state represents the state of the login flow.  choose_method: ask the user to choose a method (e.g. login account via email) sent_email: the email has been sent to the user passed_challenge: the request was successful and the login challenge was passed.
    """

    """
    allowed enum values
    """
    CHOOSE_METHOD = 'choose_method'
    SENT_EMAIL = 'sent_email'
    PASSED_CHALLENGE = 'passed_challenge'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LoginFlowState from a JSON string"""
        return cls(json.loads(json_str))


