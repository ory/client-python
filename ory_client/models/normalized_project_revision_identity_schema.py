# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.14.4
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
from ory_client.models.managed_identity_schema import ManagedIdentitySchema
from typing import Optional, Set
from typing_extensions import Self

class NormalizedProjectRevisionIdentitySchema(BaseModel):
    """
    NormalizedProjectRevisionIdentitySchema
    """ # noqa: E501
    created_at: Optional[datetime] = Field(default=None, description="The Project's Revision Creation Date")
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of this entry.")
    identity_schema: Optional[ManagedIdentitySchema] = None
    identity_schema_id: Optional[StrictStr] = None
    import_id: Optional[StrictStr] = Field(default=None, description="The imported (named) ID of the Identity Schema referenced in the Ory Kratos config.")
    import_url: Optional[StrictStr] = Field(default=None, description="The ImportURL can be used to import an Identity Schema from a bse64 encoded string. In the future, this key also support HTTPS and other sources!  If you import an Ory Kratos configuration, this would be akin to the `identity.schemas.#.url` key.  The configuration will always return the import URL when you fetch it from the API.")
    is_default: Optional[StrictBool] = Field(default=None, description="If true sets the default schema for identities  Only one schema can ever be the default schema. If you try to add two schemas with default to true, the request will fail.")
    preset: Optional[StrictStr] = Field(default=None, description="Use a preset instead of a custom identity schema.")
    project_revision_id: Optional[StrictStr] = Field(default=None, description="The Revision's ID this schema belongs to")
    updated_at: Optional[datetime] = Field(default=None, description="Last Time Project's Revision was Updated")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["created_at", "id", "identity_schema", "identity_schema_id", "import_id", "import_url", "is_default", "preset", "project_revision_id", "updated_at"]

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
        """Create an instance of NormalizedProjectRevisionIdentitySchema from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of identity_schema
        if self.identity_schema:
            _dict['identity_schema'] = self.identity_schema.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if identity_schema_id (nullable) is None
        # and model_fields_set contains the field
        if self.identity_schema_id is None and "identity_schema_id" in self.model_fields_set:
            _dict['identity_schema_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormalizedProjectRevisionIdentitySchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "identity_schema": ManagedIdentitySchema.from_dict(obj["identity_schema"]) if obj.get("identity_schema") is not None else None,
            "identity_schema_id": obj.get("identity_schema_id"),
            "import_id": obj.get("import_id"),
            "import_url": obj.get("import_url"),
            "is_default": obj.get("is_default"),
            "preset": obj.get("preset"),
            "project_revision_id": obj.get("project_revision_id"),
            "updated_at": obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


