# coding: utf-8

"""
    Ory APIs

    # Introduction Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.  ## SDKs This document describes the APIs available in the Ory Network. The APIs are available as SDKs for the following languages:  | Language       | Download SDK                                                     | Documentation                                                                        | | -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ | | Dart           | [pub.dev](https://pub.dev/packages/ory_client)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/dart/README.md)       | | .NET           | [nuget.org](https://www.nuget.org/packages/Ory.Client/)          | [README](https://github.com/ory/sdk/blob/master/clients/client/dotnet/README.md)     | | Elixir         | [hex.pm](https://hex.pm/packages/ory_client)                     | [README](https://github.com/ory/sdk/blob/master/clients/client/elixir/README.md)     | | Go             | [github.com](https://github.com/ory/client-go)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/go/README.md)         | | Java           | [maven.org](https://search.maven.org/artifact/sh.ory/ory-client) | [README](https://github.com/ory/sdk/blob/master/clients/client/java/README.md)       | | JavaScript     | [npmjs.com](https://www.npmjs.com/package/@ory/client)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript/README.md) | | JavaScript (With fetch) | [npmjs.com](https://www.npmjs.com/package/@ory/client-fetch)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript-fetch/README.md) |  | PHP            | [packagist.org](https://packagist.org/packages/ory/client)       | [README](https://github.com/ory/sdk/blob/master/clients/client/php/README.md)        | | Python         | [pypi.org](https://pypi.org/project/ory-client/)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/python/README.md)     | | Ruby           | [rubygems.org](https://rubygems.org/gems/ory-client)             | [README](https://github.com/ory/sdk/blob/master/clients/client/ruby/README.md)       | | Rust           | [crates.io](https://crates.io/crates/ory-client)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/rust/README.md)       | 

    The version of the OpenAPI document: v1.20.7
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from ory_client.models.ui_node_anchor_attributes import UiNodeAnchorAttributes
from ory_client.models.ui_node_division_attributes import UiNodeDivisionAttributes
from ory_client.models.ui_node_image_attributes import UiNodeImageAttributes
from ory_client.models.ui_node_input_attributes import UiNodeInputAttributes
from ory_client.models.ui_node_script_attributes import UiNodeScriptAttributes
from ory_client.models.ui_node_text_attributes import UiNodeTextAttributes
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

UINODEATTRIBUTES_ONE_OF_SCHEMAS = ["UiNodeAnchorAttributes", "UiNodeDivisionAttributes", "UiNodeImageAttributes", "UiNodeInputAttributes", "UiNodeScriptAttributes", "UiNodeTextAttributes"]

class UiNodeAttributes(BaseModel):
    """
    UiNodeAttributes
    """
    # data type: UiNodeInputAttributes
    oneof_schema_1_validator: Optional[UiNodeInputAttributes] = None
    # data type: UiNodeTextAttributes
    oneof_schema_2_validator: Optional[UiNodeTextAttributes] = None
    # data type: UiNodeImageAttributes
    oneof_schema_3_validator: Optional[UiNodeImageAttributes] = None
    # data type: UiNodeAnchorAttributes
    oneof_schema_4_validator: Optional[UiNodeAnchorAttributes] = None
    # data type: UiNodeScriptAttributes
    oneof_schema_5_validator: Optional[UiNodeScriptAttributes] = None
    # data type: UiNodeDivisionAttributes
    oneof_schema_6_validator: Optional[UiNodeDivisionAttributes] = None
    actual_instance: Optional[Union[UiNodeAnchorAttributes, UiNodeDivisionAttributes, UiNodeImageAttributes, UiNodeInputAttributes, UiNodeScriptAttributes, UiNodeTextAttributes]] = None
    one_of_schemas: Set[str] = { "UiNodeAnchorAttributes", "UiNodeDivisionAttributes", "UiNodeImageAttributes", "UiNodeInputAttributes", "UiNodeScriptAttributes", "UiNodeTextAttributes" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = UiNodeAttributes.model_construct()
        error_messages = []
        match = 0
        # validate data type: UiNodeInputAttributes
        if not isinstance(v, UiNodeInputAttributes):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UiNodeInputAttributes`")
        else:
            match += 1
        # validate data type: UiNodeTextAttributes
        if not isinstance(v, UiNodeTextAttributes):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UiNodeTextAttributes`")
        else:
            match += 1
        # validate data type: UiNodeImageAttributes
        if not isinstance(v, UiNodeImageAttributes):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UiNodeImageAttributes`")
        else:
            match += 1
        # validate data type: UiNodeAnchorAttributes
        if not isinstance(v, UiNodeAnchorAttributes):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UiNodeAnchorAttributes`")
        else:
            match += 1
        # validate data type: UiNodeScriptAttributes
        if not isinstance(v, UiNodeScriptAttributes):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UiNodeScriptAttributes`")
        else:
            match += 1
        # validate data type: UiNodeDivisionAttributes
        if not isinstance(v, UiNodeDivisionAttributes):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UiNodeDivisionAttributes`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in UiNodeAttributes with oneOf schemas: UiNodeAnchorAttributes, UiNodeDivisionAttributes, UiNodeImageAttributes, UiNodeInputAttributes, UiNodeScriptAttributes, UiNodeTextAttributes. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in UiNodeAttributes with oneOf schemas: UiNodeAnchorAttributes, UiNodeDivisionAttributes, UiNodeImageAttributes, UiNodeInputAttributes, UiNodeScriptAttributes, UiNodeTextAttributes. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("node_type")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `node_type` in the input.")

        # check if data type is `UiNodeAnchorAttributes`
        if _data_type == "a":
            instance.actual_instance = UiNodeAnchorAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeDivisionAttributes`
        if _data_type == "div":
            instance.actual_instance = UiNodeDivisionAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeImageAttributes`
        if _data_type == "img":
            instance.actual_instance = UiNodeImageAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeInputAttributes`
        if _data_type == "input":
            instance.actual_instance = UiNodeInputAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeScriptAttributes`
        if _data_type == "script":
            instance.actual_instance = UiNodeScriptAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeTextAttributes`
        if _data_type == "text":
            instance.actual_instance = UiNodeTextAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeAnchorAttributes`
        if _data_type == "uiNodeAnchorAttributes":
            instance.actual_instance = UiNodeAnchorAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeDivisionAttributes`
        if _data_type == "uiNodeDivisionAttributes":
            instance.actual_instance = UiNodeDivisionAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeImageAttributes`
        if _data_type == "uiNodeImageAttributes":
            instance.actual_instance = UiNodeImageAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeInputAttributes`
        if _data_type == "uiNodeInputAttributes":
            instance.actual_instance = UiNodeInputAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeScriptAttributes`
        if _data_type == "uiNodeScriptAttributes":
            instance.actual_instance = UiNodeScriptAttributes.from_json(json_str)
            return instance

        # check if data type is `UiNodeTextAttributes`
        if _data_type == "uiNodeTextAttributes":
            instance.actual_instance = UiNodeTextAttributes.from_json(json_str)
            return instance

        # deserialize data into UiNodeInputAttributes
        try:
            instance.actual_instance = UiNodeInputAttributes.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UiNodeTextAttributes
        try:
            instance.actual_instance = UiNodeTextAttributes.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UiNodeImageAttributes
        try:
            instance.actual_instance = UiNodeImageAttributes.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UiNodeAnchorAttributes
        try:
            instance.actual_instance = UiNodeAnchorAttributes.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UiNodeScriptAttributes
        try:
            instance.actual_instance = UiNodeScriptAttributes.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UiNodeDivisionAttributes
        try:
            instance.actual_instance = UiNodeDivisionAttributes.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into UiNodeAttributes with oneOf schemas: UiNodeAnchorAttributes, UiNodeDivisionAttributes, UiNodeImageAttributes, UiNodeInputAttributes, UiNodeScriptAttributes, UiNodeTextAttributes. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UiNodeAttributes with oneOf schemas: UiNodeAnchorAttributes, UiNodeDivisionAttributes, UiNodeImageAttributes, UiNodeInputAttributes, UiNodeScriptAttributes, UiNodeTextAttributes. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], UiNodeAnchorAttributes, UiNodeDivisionAttributes, UiNodeImageAttributes, UiNodeInputAttributes, UiNodeScriptAttributes, UiNodeTextAttributes]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


