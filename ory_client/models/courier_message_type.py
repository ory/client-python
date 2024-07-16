# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.14.0
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CourierMessageType(str, Enum):
    """
    It can either be `email` or `phone`
    """

    """
    allowed enum values
    """
    EMAIL = 'email'
    PHONE = 'phone'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CourierMessageType from a JSON string"""
        return cls(json.loads(json_str))


