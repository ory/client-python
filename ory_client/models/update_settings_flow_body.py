# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.6
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from ory_client.models.update_settings_flow_with_lookup_method import UpdateSettingsFlowWithLookupMethod
from ory_client.models.update_settings_flow_with_oidc_method import UpdateSettingsFlowWithOidcMethod
from ory_client.models.update_settings_flow_with_passkey_method import UpdateSettingsFlowWithPasskeyMethod
from ory_client.models.update_settings_flow_with_password_method import UpdateSettingsFlowWithPasswordMethod
from ory_client.models.update_settings_flow_with_profile_method import UpdateSettingsFlowWithProfileMethod
from ory_client.models.update_settings_flow_with_totp_method import UpdateSettingsFlowWithTotpMethod
from ory_client.models.update_settings_flow_with_web_authn_method import UpdateSettingsFlowWithWebAuthnMethod
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

UPDATESETTINGSFLOWBODY_ONE_OF_SCHEMAS = ["UpdateSettingsFlowWithLookupMethod", "UpdateSettingsFlowWithOidcMethod", "UpdateSettingsFlowWithPasskeyMethod", "UpdateSettingsFlowWithPasswordMethod", "UpdateSettingsFlowWithProfileMethod", "UpdateSettingsFlowWithTotpMethod", "UpdateSettingsFlowWithWebAuthnMethod"]

class UpdateSettingsFlowBody(BaseModel):
    """
    Update Settings Flow Request Body
    """
    # data type: UpdateSettingsFlowWithPasswordMethod
    oneof_schema_1_validator: Optional[UpdateSettingsFlowWithPasswordMethod] = None
    # data type: UpdateSettingsFlowWithProfileMethod
    oneof_schema_2_validator: Optional[UpdateSettingsFlowWithProfileMethod] = None
    # data type: UpdateSettingsFlowWithOidcMethod
    oneof_schema_3_validator: Optional[UpdateSettingsFlowWithOidcMethod] = None
    # data type: UpdateSettingsFlowWithTotpMethod
    oneof_schema_4_validator: Optional[UpdateSettingsFlowWithTotpMethod] = None
    # data type: UpdateSettingsFlowWithWebAuthnMethod
    oneof_schema_5_validator: Optional[UpdateSettingsFlowWithWebAuthnMethod] = None
    # data type: UpdateSettingsFlowWithLookupMethod
    oneof_schema_6_validator: Optional[UpdateSettingsFlowWithLookupMethod] = None
    # data type: UpdateSettingsFlowWithPasskeyMethod
    oneof_schema_7_validator: Optional[UpdateSettingsFlowWithPasskeyMethod] = None
    actual_instance: Optional[Union[UpdateSettingsFlowWithLookupMethod, UpdateSettingsFlowWithOidcMethod, UpdateSettingsFlowWithPasskeyMethod, UpdateSettingsFlowWithPasswordMethod, UpdateSettingsFlowWithProfileMethod, UpdateSettingsFlowWithTotpMethod, UpdateSettingsFlowWithWebAuthnMethod]] = None
    one_of_schemas: Set[str] = { "UpdateSettingsFlowWithLookupMethod", "UpdateSettingsFlowWithOidcMethod", "UpdateSettingsFlowWithPasskeyMethod", "UpdateSettingsFlowWithPasswordMethod", "UpdateSettingsFlowWithProfileMethod", "UpdateSettingsFlowWithTotpMethod", "UpdateSettingsFlowWithWebAuthnMethod" }

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
        instance = UpdateSettingsFlowBody.model_construct()
        error_messages = []
        match = 0
        # validate data type: UpdateSettingsFlowWithPasswordMethod
        if not isinstance(v, UpdateSettingsFlowWithPasswordMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateSettingsFlowWithPasswordMethod`")
        else:
            match += 1
        # validate data type: UpdateSettingsFlowWithProfileMethod
        if not isinstance(v, UpdateSettingsFlowWithProfileMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateSettingsFlowWithProfileMethod`")
        else:
            match += 1
        # validate data type: UpdateSettingsFlowWithOidcMethod
        if not isinstance(v, UpdateSettingsFlowWithOidcMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateSettingsFlowWithOidcMethod`")
        else:
            match += 1
        # validate data type: UpdateSettingsFlowWithTotpMethod
        if not isinstance(v, UpdateSettingsFlowWithTotpMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateSettingsFlowWithTotpMethod`")
        else:
            match += 1
        # validate data type: UpdateSettingsFlowWithWebAuthnMethod
        if not isinstance(v, UpdateSettingsFlowWithWebAuthnMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateSettingsFlowWithWebAuthnMethod`")
        else:
            match += 1
        # validate data type: UpdateSettingsFlowWithLookupMethod
        if not isinstance(v, UpdateSettingsFlowWithLookupMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateSettingsFlowWithLookupMethod`")
        else:
            match += 1
        # validate data type: UpdateSettingsFlowWithPasskeyMethod
        if not isinstance(v, UpdateSettingsFlowWithPasskeyMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateSettingsFlowWithPasskeyMethod`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in UpdateSettingsFlowBody with oneOf schemas: UpdateSettingsFlowWithLookupMethod, UpdateSettingsFlowWithOidcMethod, UpdateSettingsFlowWithPasskeyMethod, UpdateSettingsFlowWithPasswordMethod, UpdateSettingsFlowWithProfileMethod, UpdateSettingsFlowWithTotpMethod, UpdateSettingsFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in UpdateSettingsFlowBody with oneOf schemas: UpdateSettingsFlowWithLookupMethod, UpdateSettingsFlowWithOidcMethod, UpdateSettingsFlowWithPasskeyMethod, UpdateSettingsFlowWithPasswordMethod, UpdateSettingsFlowWithProfileMethod, UpdateSettingsFlowWithTotpMethod, UpdateSettingsFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
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
        _data_type = json.loads(json_str).get("method")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `method` in the input.")

        # check if data type is `UpdateSettingsFlowWithLookupMethod`
        if _data_type == "lookup_secret":
            instance.actual_instance = UpdateSettingsFlowWithLookupMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithOidcMethod`
        if _data_type == "oidc":
            instance.actual_instance = UpdateSettingsFlowWithOidcMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithPasskeyMethod`
        if _data_type == "passkey":
            instance.actual_instance = UpdateSettingsFlowWithPasskeyMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithPasswordMethod`
        if _data_type == "password":
            instance.actual_instance = UpdateSettingsFlowWithPasswordMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithProfileMethod`
        if _data_type == "profile":
            instance.actual_instance = UpdateSettingsFlowWithProfileMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithTotpMethod`
        if _data_type == "totp":
            instance.actual_instance = UpdateSettingsFlowWithTotpMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithWebAuthnMethod`
        if _data_type == "webauthn":
            instance.actual_instance = UpdateSettingsFlowWithWebAuthnMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithLookupMethod`
        if _data_type == "updateSettingsFlowWithLookupMethod":
            instance.actual_instance = UpdateSettingsFlowWithLookupMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithOidcMethod`
        if _data_type == "updateSettingsFlowWithOidcMethod":
            instance.actual_instance = UpdateSettingsFlowWithOidcMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithPasskeyMethod`
        if _data_type == "updateSettingsFlowWithPasskeyMethod":
            instance.actual_instance = UpdateSettingsFlowWithPasskeyMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithPasswordMethod`
        if _data_type == "updateSettingsFlowWithPasswordMethod":
            instance.actual_instance = UpdateSettingsFlowWithPasswordMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithProfileMethod`
        if _data_type == "updateSettingsFlowWithProfileMethod":
            instance.actual_instance = UpdateSettingsFlowWithProfileMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithTotpMethod`
        if _data_type == "updateSettingsFlowWithTotpMethod":
            instance.actual_instance = UpdateSettingsFlowWithTotpMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateSettingsFlowWithWebAuthnMethod`
        if _data_type == "updateSettingsFlowWithWebAuthnMethod":
            instance.actual_instance = UpdateSettingsFlowWithWebAuthnMethod.from_json(json_str)
            return instance

        # deserialize data into UpdateSettingsFlowWithPasswordMethod
        try:
            instance.actual_instance = UpdateSettingsFlowWithPasswordMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateSettingsFlowWithProfileMethod
        try:
            instance.actual_instance = UpdateSettingsFlowWithProfileMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateSettingsFlowWithOidcMethod
        try:
            instance.actual_instance = UpdateSettingsFlowWithOidcMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateSettingsFlowWithTotpMethod
        try:
            instance.actual_instance = UpdateSettingsFlowWithTotpMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateSettingsFlowWithWebAuthnMethod
        try:
            instance.actual_instance = UpdateSettingsFlowWithWebAuthnMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateSettingsFlowWithLookupMethod
        try:
            instance.actual_instance = UpdateSettingsFlowWithLookupMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateSettingsFlowWithPasskeyMethod
        try:
            instance.actual_instance = UpdateSettingsFlowWithPasskeyMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into UpdateSettingsFlowBody with oneOf schemas: UpdateSettingsFlowWithLookupMethod, UpdateSettingsFlowWithOidcMethod, UpdateSettingsFlowWithPasskeyMethod, UpdateSettingsFlowWithPasswordMethod, UpdateSettingsFlowWithProfileMethod, UpdateSettingsFlowWithTotpMethod, UpdateSettingsFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UpdateSettingsFlowBody with oneOf schemas: UpdateSettingsFlowWithLookupMethod, UpdateSettingsFlowWithOidcMethod, UpdateSettingsFlowWithPasskeyMethod, UpdateSettingsFlowWithPasswordMethod, UpdateSettingsFlowWithProfileMethod, UpdateSettingsFlowWithTotpMethod, UpdateSettingsFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], UpdateSettingsFlowWithLookupMethod, UpdateSettingsFlowWithOidcMethod, UpdateSettingsFlowWithPasskeyMethod, UpdateSettingsFlowWithPasswordMethod, UpdateSettingsFlowWithProfileMethod, UpdateSettingsFlowWithTotpMethod, UpdateSettingsFlowWithWebAuthnMethod]]:
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


