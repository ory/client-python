# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.12.2
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class VerifiableIdentityAddress(BaseModel):
    """
    VerifiableAddress is an identity's verifiable address
    """ # noqa: E501
    created_at: Optional[datetime] = Field(default=None, description="When this entry was created")
    id: Optional[StrictStr] = Field(default=None, description="The ID")
    status: StrictStr = Field(description="VerifiableAddressStatus must not exceed 16 characters as that is the limitation in the SQL Schema")
    updated_at: Optional[datetime] = Field(default=None, description="When this entry was last updated")
    value: StrictStr = Field(description="The address value  example foo@user.com")
    verified: StrictBool = Field(description="Indicates if the address has already been verified")
    verified_at: Optional[datetime] = None
    via: StrictStr = Field(description="The delivery method")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["created_at", "id", "status", "updated_at", "value", "verified", "verified_at", "via"]

    @field_validator('via')
    def via_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['email', 'sms']):
            raise ValueError("must be one of enum values ('email', 'sms')")
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
        """Create an instance of VerifiableIdentityAddress from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VerifiableIdentityAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "status": obj.get("status"),
            "updated_at": obj.get("updated_at"),
            "value": obj.get("value"),
            "verified": obj.get("verified"),
            "verified_at": obj.get("verified_at"),
            "via": obj.get("via")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


