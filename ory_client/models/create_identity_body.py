# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.1
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from ory_client.models.identity_with_credentials import IdentityWithCredentials
from ory_client.models.recovery_identity_address import RecoveryIdentityAddress
from ory_client.models.verifiable_identity_address import VerifiableIdentityAddress
from typing import Optional, Set
from typing_extensions import Self

class CreateIdentityBody(BaseModel):
    """
    Create Identity Body
    """ # noqa: E501
    credentials: Optional[IdentityWithCredentials] = None
    metadata_admin: Optional[Any] = Field(default=None, description="Store metadata about the user which is only accessible through admin APIs such as `GET /admin/identities/<id>`.")
    metadata_public: Optional[Any] = Field(default=None, description="Store metadata about the identity which the identity itself can see when calling for example the session endpoint. Do not store sensitive information (e.g. credit score) about the identity in this field.")
    recovery_addresses: Optional[List[RecoveryIdentityAddress]] = Field(default=None, description="RecoveryAddresses contains all the addresses that can be used to recover an identity.  Use this structure to import recovery addresses for an identity. Please keep in mind that the address needs to be represented in the Identity Schema or this field will be overwritten on the next identity update.")
    schema_id: StrictStr = Field(description="SchemaID is the ID of the JSON Schema to be used for validating the identity's traits.")
    state: Optional[StrictStr] = Field(default=None, description="State is the identity's state. active StateActive inactive StateInactive")
    traits: Dict[str, Any] = Field(description="Traits represent an identity's traits. The identity is able to create, modify, and delete traits in a self-service manner. The input will always be validated against the JSON Schema defined in `schema_url`.")
    verifiable_addresses: Optional[List[VerifiableIdentityAddress]] = Field(default=None, description="VerifiableAddresses contains all the addresses that can be verified by the user.  Use this structure to import verified addresses for an identity. Please keep in mind that the address needs to be represented in the Identity Schema or this field will be overwritten on the next identity update.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["credentials", "metadata_admin", "metadata_public", "recovery_addresses", "schema_id", "state", "traits", "verifiable_addresses"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['active', 'inactive']):
            raise ValueError("must be one of enum values ('active', 'inactive')")
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
        """Create an instance of CreateIdentityBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in recovery_addresses (list)
        _items = []
        if self.recovery_addresses:
            for _item in self.recovery_addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recovery_addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in verifiable_addresses (list)
        _items = []
        if self.verifiable_addresses:
            for _item in self.verifiable_addresses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['verifiable_addresses'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if metadata_admin (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_admin is None and "metadata_admin" in self.model_fields_set:
            _dict['metadata_admin'] = None

        # set to None if metadata_public (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_public is None and "metadata_public" in self.model_fields_set:
            _dict['metadata_public'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateIdentityBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "credentials": IdentityWithCredentials.from_dict(obj["credentials"]) if obj.get("credentials") is not None else None,
            "metadata_admin": obj.get("metadata_admin"),
            "metadata_public": obj.get("metadata_public"),
            "recovery_addresses": [RecoveryIdentityAddress.from_dict(_item) for _item in obj["recovery_addresses"]] if obj.get("recovery_addresses") is not None else None,
            "schema_id": obj.get("schema_id"),
            "state": obj.get("state"),
            "traits": obj.get("traits"),
            "verifiable_addresses": [VerifiableIdentityAddress.from_dict(_item) for _item in obj["verifiable_addresses"]] if obj.get("verifiable_addresses") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


