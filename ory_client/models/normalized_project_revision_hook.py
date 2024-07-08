# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.3
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NormalizedProjectRevisionHook(BaseModel):
    """
    NormalizedProjectRevisionHook
    """ # noqa: E501
    config_key: StrictStr = Field(description="The Hooks Config Key")
    created_at: Optional[datetime] = Field(default=None, description="The Project's Revision Creation Date")
    hook: StrictStr = Field(description="The Hook Type")
    id: Optional[StrictStr] = Field(default=None, description="ID of the entry")
    project_revision_id: Optional[StrictStr] = Field(default=None, description="The Revision's ID this schema belongs to")
    updated_at: Optional[datetime] = Field(default=None, description="Last Time Project's Revision was Updated")
    web_hook_config_auth_api_key_in: Optional[StrictStr] = Field(default=None, description="Whether to send the API Key in the HTTP Header or as a HTTP Cookie")
    web_hook_config_auth_api_key_name: Optional[StrictStr] = Field(default=None, description="The name of the api key")
    web_hook_config_auth_api_key_value: Optional[StrictStr] = Field(default=None, description="The value of the api key")
    web_hook_config_auth_basic_auth_password: Optional[StrictStr] = Field(default=None, description="The password to be sent in the HTTP Basic Auth Header")
    web_hook_config_auth_basic_auth_user: Optional[StrictStr] = Field(default=None, description="The username to be sent in the HTTP Basic Auth Header")
    web_hook_config_auth_type: Optional[StrictStr] = Field(default=None, description="HTTP Auth Method to use for the Web-Hook")
    web_hook_config_body: Optional[StrictStr] = Field(default=None, description="URI pointing to the JsonNet template used for Web-Hook payload generation. Only used for those HTTP methods, which support HTTP body payloads.")
    web_hook_config_can_interrupt: Optional[StrictBool] = Field(default=None, description="If enabled allows the web hook to interrupt / abort the self-service flow. It only applies to certain flows (registration/verification/login/settings) and requires a valid response format.")
    web_hook_config_method: Optional[StrictStr] = Field(default=None, description="The HTTP method to use (GET, POST, etc) for the Web-Hook")
    web_hook_config_response_ignore: Optional[StrictBool] = Field(default=None, description="Whether to ignore the Web Hook response")
    web_hook_config_response_parse: Optional[StrictBool] = Field(default=None, description="Whether to parse the Web Hook response")
    web_hook_config_url: Optional[StrictStr] = Field(default=None, description="The URL the Web-Hook should call")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["config_key", "created_at", "hook", "id", "project_revision_id", "updated_at", "web_hook_config_auth_api_key_in", "web_hook_config_auth_api_key_name", "web_hook_config_auth_api_key_value", "web_hook_config_auth_basic_auth_password", "web_hook_config_auth_basic_auth_user", "web_hook_config_auth_type", "web_hook_config_body", "web_hook_config_can_interrupt", "web_hook_config_method", "web_hook_config_response_ignore", "web_hook_config_response_parse", "web_hook_config_url"]

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
        """Create an instance of NormalizedProjectRevisionHook from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "updated_at",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormalizedProjectRevisionHook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config_key": obj.get("config_key"),
            "created_at": obj.get("created_at"),
            "hook": obj.get("hook"),
            "id": obj.get("id"),
            "project_revision_id": obj.get("project_revision_id"),
            "updated_at": obj.get("updated_at"),
            "web_hook_config_auth_api_key_in": obj.get("web_hook_config_auth_api_key_in"),
            "web_hook_config_auth_api_key_name": obj.get("web_hook_config_auth_api_key_name"),
            "web_hook_config_auth_api_key_value": obj.get("web_hook_config_auth_api_key_value"),
            "web_hook_config_auth_basic_auth_password": obj.get("web_hook_config_auth_basic_auth_password"),
            "web_hook_config_auth_basic_auth_user": obj.get("web_hook_config_auth_basic_auth_user"),
            "web_hook_config_auth_type": obj.get("web_hook_config_auth_type"),
            "web_hook_config_body": obj.get("web_hook_config_body"),
            "web_hook_config_can_interrupt": obj.get("web_hook_config_can_interrupt"),
            "web_hook_config_method": obj.get("web_hook_config_method"),
            "web_hook_config_response_ignore": obj.get("web_hook_config_response_ignore"),
            "web_hook_config_response_parse": obj.get("web_hook_config_response_parse"),
            "web_hook_config_url": obj.get("web_hook_config_url")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


