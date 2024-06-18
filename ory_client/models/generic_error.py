# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.11.10
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ory_client.models.generic_error_content import GenericErrorContent
from typing import Optional, Set
from typing_extensions import Self

class GenericError(BaseModel):
    """
    Error responses are sent when an error (e.g. unauthorized, bad request, ...) occurred.
    """ # noqa: E501
    code: Optional[StrictInt] = Field(default=None, description="The status code")
    debug: Optional[StrictStr] = Field(default=None, description="Debug information  This field is often not exposed to protect against leaking sensitive information.")
    details: Optional[Any] = Field(default=None, description="Further error details")
    error: Optional[GenericErrorContent] = None
    id: Optional[StrictStr] = Field(default=None, description="The error ID  Useful when trying to identify various errors in application logic.")
    message: StrictStr = Field(description="Error message  The error's message.")
    reason: Optional[StrictStr] = Field(default=None, description="A human-readable reason for the error")
    request: Optional[StrictStr] = Field(default=None, description="The request ID  The request ID is often exposed internally in order to trace errors across service architectures. This is often a UUID.")
    status: Optional[StrictStr] = Field(default=None, description="The status description")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["code", "debug", "details", "error", "id", "message", "reason", "request", "status"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GenericError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenericError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "debug": obj.get("debug"),
            "details": obj.get("details"),
            "error": GenericErrorContent.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "id": obj.get("id"),
            "message": obj.get("message"),
            "reason": obj.get("reason"),
            "request": obj.get("request"),
            "status": obj.get("status")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

