# coding: utf-8

"""
    Ory APIs

    # Introduction Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.  ## SDKs This document describes the APIs available in the Ory Network. The APIs are available as SDKs for the following languages:  | Language       | Download SDK                                                     | Documentation                                                                        | | -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ | | Dart           | [pub.dev](https://pub.dev/packages/ory_client)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/dart/README.md)       | | .NET           | [nuget.org](https://www.nuget.org/packages/Ory.Client/)          | [README](https://github.com/ory/sdk/blob/master/clients/client/dotnet/README.md)     | | Elixir         | [hex.pm](https://hex.pm/packages/ory_client)                     | [README](https://github.com/ory/sdk/blob/master/clients/client/elixir/README.md)     | | Go             | [github.com](https://github.com/ory/client-go)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/go/README.md)         | | Java           | [maven.org](https://search.maven.org/artifact/sh.ory/ory-client) | [README](https://github.com/ory/sdk/blob/master/clients/client/java/README.md)       | | JavaScript     | [npmjs.com](https://www.npmjs.com/package/@ory/client)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript/README.md) | | JavaScript (With fetch) | [npmjs.com](https://www.npmjs.com/package/@ory/client-fetch)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript-fetch/README.md) |  | PHP            | [packagist.org](https://packagist.org/packages/ory/client)       | [README](https://github.com/ory/sdk/blob/master/clients/client/php/README.md)        | | Python         | [pypi.org](https://pypi.org/project/ory-client/)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/python/README.md)     | | Ruby           | [rubygems.org](https://rubygems.org/gems/ory-client)             | [README](https://github.com/ory/sdk/blob/master/clients/client/ruby/README.md)       | | Rust           | [crates.io](https://crates.io/crates/ory-client)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/rust/README.md)       | 

    The version of the OpenAPI document: v1.17.1
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NormalizedProjectRevisionCourierChannel(BaseModel):
    """
    NormalizedProjectRevisionCourierChannel
    """ # noqa: E501
    channel_id: StrictStr = Field(description="The Channel's public ID")
    created_at: Optional[datetime] = Field(default=None, description="The creation date")
    request_config_auth_config_api_key_in: Optional[StrictStr] = Field(default=None, description="API key location  Can either be \"header\" or \"query\"")
    request_config_auth_config_api_key_name: Optional[StrictStr] = Field(default=None, description="API key name  Only used if the auth type is api_key")
    request_config_auth_config_api_key_value: Optional[StrictStr] = Field(default=None, description="API key value  Only used if the auth type is api_key")
    request_config_auth_config_basic_auth_password: Optional[StrictStr] = Field(default=None, description="Basic Auth Password  Only used if the auth type is basic_auth")
    request_config_auth_config_basic_auth_user: Optional[StrictStr] = Field(default=None, description="Basic Auth Username  Only used if the auth type is basic_auth")
    request_config_auth_type: Optional[StrictStr] = Field(default=None, description="HTTP Auth Method to use for the HTTP call  Can either be basic_auth or api_key basic_auth CourierChannelAuthTypeBasicAuth api_key CourierChannelAuthTypeApiKey")
    request_config_body: StrictStr = Field(description="URI pointing to the JsonNet template used for HTTP body payload generation.")
    request_config_headers: Optional[Dict[str, Any]] = Field(default=None, description="NullJSONRawMessage represents a json.RawMessage that works well with JSON, SQL, and Swagger and is NULLable-")
    request_config_method: StrictStr = Field(description="The HTTP method to use (GET, POST, etc) for the HTTP call")
    request_config_url: Optional[StrictStr] = None
    updated_at: Optional[datetime] = Field(default=None, description="Last upate time")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["channel_id", "created_at", "request_config_auth_config_api_key_in", "request_config_auth_config_api_key_name", "request_config_auth_config_api_key_value", "request_config_auth_config_basic_auth_password", "request_config_auth_config_basic_auth_user", "request_config_auth_type", "request_config_body", "request_config_headers", "request_config_method", "request_config_url", "updated_at"]

    @field_validator('request_config_auth_type')
    def request_config_auth_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['basic_auth', 'api_key']):
            raise ValueError("must be one of enum values ('basic_auth', 'api_key')")
        return value

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
        """Create an instance of NormalizedProjectRevisionCourierChannel from a JSON string"""
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

        # set to None if request_config_headers (nullable) is None
        # and model_fields_set contains the field
        if self.request_config_headers is None and "request_config_headers" in self.model_fields_set:
            _dict['request_config_headers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormalizedProjectRevisionCourierChannel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "channel_id": obj.get("channel_id"),
            "created_at": obj.get("created_at"),
            "request_config_auth_config_api_key_in": obj.get("request_config_auth_config_api_key_in"),
            "request_config_auth_config_api_key_name": obj.get("request_config_auth_config_api_key_name"),
            "request_config_auth_config_api_key_value": obj.get("request_config_auth_config_api_key_value"),
            "request_config_auth_config_basic_auth_password": obj.get("request_config_auth_config_basic_auth_password"),
            "request_config_auth_config_basic_auth_user": obj.get("request_config_auth_config_basic_auth_user"),
            "request_config_auth_type": obj.get("request_config_auth_type"),
            "request_config_body": obj.get("request_config_body"),
            "request_config_headers": obj.get("request_config_headers"),
            "request_config_method": obj.get("request_config_method"),
            "request_config_url": obj.get("request_config_url"),
            "updated_at": obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


