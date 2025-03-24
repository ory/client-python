# coding: utf-8

"""
    Ory APIs

    # Introduction Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.  ## SDKs This document describes the APIs available in the Ory Network. The APIs are available as SDKs for the following languages:  | Language       | Download SDK                                                     | Documentation                                                                        | | -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ | | Dart           | [pub.dev](https://pub.dev/packages/ory_client)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/dart/README.md)       | | .NET           | [nuget.org](https://www.nuget.org/packages/Ory.Client/)          | [README](https://github.com/ory/sdk/blob/master/clients/client/dotnet/README.md)     | | Elixir         | [hex.pm](https://hex.pm/packages/ory_client)                     | [README](https://github.com/ory/sdk/blob/master/clients/client/elixir/README.md)     | | Go             | [github.com](https://github.com/ory/client-go)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/go/README.md)         | | Java           | [maven.org](https://search.maven.org/artifact/sh.ory/ory-client) | [README](https://github.com/ory/sdk/blob/master/clients/client/java/README.md)       | | JavaScript     | [npmjs.com](https://www.npmjs.com/package/@ory/client)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript/README.md) | | JavaScript (With fetch) | [npmjs.com](https://www.npmjs.com/package/@ory/client-fetch)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript-fetch/README.md) |  | PHP            | [packagist.org](https://packagist.org/packages/ory/client)       | [README](https://github.com/ory/sdk/blob/master/clients/client/php/README.md)        | | Python         | [pypi.org](https://pypi.org/project/ory-client/)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/python/README.md)     | | Ruby           | [rubygems.org](https://rubygems.org/gems/ory-client)             | [README](https://github.com/ory/sdk/blob/master/clients/client/ruby/README.md)       | | Rust           | [crates.io](https://crates.io/crates/ory-client)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/rust/README.md)       | 

    The version of the OpenAPI document: v1.19.0
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from ory_client.models.update_registration_flow_with_code_method import UpdateRegistrationFlowWithCodeMethod
from ory_client.models.update_registration_flow_with_oidc_method import UpdateRegistrationFlowWithOidcMethod
from ory_client.models.update_registration_flow_with_passkey_method import UpdateRegistrationFlowWithPasskeyMethod
from ory_client.models.update_registration_flow_with_password_method import UpdateRegistrationFlowWithPasswordMethod
from ory_client.models.update_registration_flow_with_profile_method import UpdateRegistrationFlowWithProfileMethod
from ory_client.models.update_registration_flow_with_saml_method import UpdateRegistrationFlowWithSamlMethod
from ory_client.models.update_registration_flow_with_web_authn_method import UpdateRegistrationFlowWithWebAuthnMethod
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

UPDATEREGISTRATIONFLOWBODY_ONE_OF_SCHEMAS = ["UpdateRegistrationFlowWithCodeMethod", "UpdateRegistrationFlowWithOidcMethod", "UpdateRegistrationFlowWithPasskeyMethod", "UpdateRegistrationFlowWithPasswordMethod", "UpdateRegistrationFlowWithProfileMethod", "UpdateRegistrationFlowWithSamlMethod", "UpdateRegistrationFlowWithWebAuthnMethod"]

class UpdateRegistrationFlowBody(BaseModel):
    """
    Update Registration Request Body
    """
    # data type: UpdateRegistrationFlowWithPasswordMethod
    oneof_schema_1_validator: Optional[UpdateRegistrationFlowWithPasswordMethod] = None
    # data type: UpdateRegistrationFlowWithOidcMethod
    oneof_schema_2_validator: Optional[UpdateRegistrationFlowWithOidcMethod] = None
    # data type: UpdateRegistrationFlowWithSamlMethod
    oneof_schema_3_validator: Optional[UpdateRegistrationFlowWithSamlMethod] = None
    # data type: UpdateRegistrationFlowWithWebAuthnMethod
    oneof_schema_4_validator: Optional[UpdateRegistrationFlowWithWebAuthnMethod] = None
    # data type: UpdateRegistrationFlowWithCodeMethod
    oneof_schema_5_validator: Optional[UpdateRegistrationFlowWithCodeMethod] = None
    # data type: UpdateRegistrationFlowWithPasskeyMethod
    oneof_schema_6_validator: Optional[UpdateRegistrationFlowWithPasskeyMethod] = None
    # data type: UpdateRegistrationFlowWithProfileMethod
    oneof_schema_7_validator: Optional[UpdateRegistrationFlowWithProfileMethod] = None
    actual_instance: Optional[Union[UpdateRegistrationFlowWithCodeMethod, UpdateRegistrationFlowWithOidcMethod, UpdateRegistrationFlowWithPasskeyMethod, UpdateRegistrationFlowWithPasswordMethod, UpdateRegistrationFlowWithProfileMethod, UpdateRegistrationFlowWithSamlMethod, UpdateRegistrationFlowWithWebAuthnMethod]] = None
    one_of_schemas: Set[str] = { "UpdateRegistrationFlowWithCodeMethod", "UpdateRegistrationFlowWithOidcMethod", "UpdateRegistrationFlowWithPasskeyMethod", "UpdateRegistrationFlowWithPasswordMethod", "UpdateRegistrationFlowWithProfileMethod", "UpdateRegistrationFlowWithSamlMethod", "UpdateRegistrationFlowWithWebAuthnMethod" }

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
        instance = UpdateRegistrationFlowBody.model_construct()
        error_messages = []
        match = 0
        # validate data type: UpdateRegistrationFlowWithPasswordMethod
        if not isinstance(v, UpdateRegistrationFlowWithPasswordMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateRegistrationFlowWithPasswordMethod`")
        else:
            match += 1
        # validate data type: UpdateRegistrationFlowWithOidcMethod
        if not isinstance(v, UpdateRegistrationFlowWithOidcMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateRegistrationFlowWithOidcMethod`")
        else:
            match += 1
        # validate data type: UpdateRegistrationFlowWithSamlMethod
        if not isinstance(v, UpdateRegistrationFlowWithSamlMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateRegistrationFlowWithSamlMethod`")
        else:
            match += 1
        # validate data type: UpdateRegistrationFlowWithWebAuthnMethod
        if not isinstance(v, UpdateRegistrationFlowWithWebAuthnMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateRegistrationFlowWithWebAuthnMethod`")
        else:
            match += 1
        # validate data type: UpdateRegistrationFlowWithCodeMethod
        if not isinstance(v, UpdateRegistrationFlowWithCodeMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateRegistrationFlowWithCodeMethod`")
        else:
            match += 1
        # validate data type: UpdateRegistrationFlowWithPasskeyMethod
        if not isinstance(v, UpdateRegistrationFlowWithPasskeyMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateRegistrationFlowWithPasskeyMethod`")
        else:
            match += 1
        # validate data type: UpdateRegistrationFlowWithProfileMethod
        if not isinstance(v, UpdateRegistrationFlowWithProfileMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateRegistrationFlowWithProfileMethod`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in UpdateRegistrationFlowBody with oneOf schemas: UpdateRegistrationFlowWithCodeMethod, UpdateRegistrationFlowWithOidcMethod, UpdateRegistrationFlowWithPasskeyMethod, UpdateRegistrationFlowWithPasswordMethod, UpdateRegistrationFlowWithProfileMethod, UpdateRegistrationFlowWithSamlMethod, UpdateRegistrationFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in UpdateRegistrationFlowBody with oneOf schemas: UpdateRegistrationFlowWithCodeMethod, UpdateRegistrationFlowWithOidcMethod, UpdateRegistrationFlowWithPasskeyMethod, UpdateRegistrationFlowWithPasswordMethod, UpdateRegistrationFlowWithProfileMethod, UpdateRegistrationFlowWithSamlMethod, UpdateRegistrationFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
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

        # check if data type is `UpdateRegistrationFlowWithCodeMethod`
        if _data_type == "code":
            instance.actual_instance = UpdateRegistrationFlowWithCodeMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithOidcMethod`
        if _data_type == "oidc":
            instance.actual_instance = UpdateRegistrationFlowWithOidcMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithPasskeyMethod`
        if _data_type == "passkey":
            instance.actual_instance = UpdateRegistrationFlowWithPasskeyMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithPasswordMethod`
        if _data_type == "password":
            instance.actual_instance = UpdateRegistrationFlowWithPasswordMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithProfileMethod`
        if _data_type == "profile":
            instance.actual_instance = UpdateRegistrationFlowWithProfileMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithSamlMethod`
        if _data_type == "saml":
            instance.actual_instance = UpdateRegistrationFlowWithSamlMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithWebAuthnMethod`
        if _data_type == "webauthn":
            instance.actual_instance = UpdateRegistrationFlowWithWebAuthnMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithCodeMethod`
        if _data_type == "updateRegistrationFlowWithCodeMethod":
            instance.actual_instance = UpdateRegistrationFlowWithCodeMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithOidcMethod`
        if _data_type == "updateRegistrationFlowWithOidcMethod":
            instance.actual_instance = UpdateRegistrationFlowWithOidcMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithPasskeyMethod`
        if _data_type == "updateRegistrationFlowWithPasskeyMethod":
            instance.actual_instance = UpdateRegistrationFlowWithPasskeyMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithPasswordMethod`
        if _data_type == "updateRegistrationFlowWithPasswordMethod":
            instance.actual_instance = UpdateRegistrationFlowWithPasswordMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithProfileMethod`
        if _data_type == "updateRegistrationFlowWithProfileMethod":
            instance.actual_instance = UpdateRegistrationFlowWithProfileMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithSamlMethod`
        if _data_type == "updateRegistrationFlowWithSamlMethod":
            instance.actual_instance = UpdateRegistrationFlowWithSamlMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateRegistrationFlowWithWebAuthnMethod`
        if _data_type == "updateRegistrationFlowWithWebAuthnMethod":
            instance.actual_instance = UpdateRegistrationFlowWithWebAuthnMethod.from_json(json_str)
            return instance

        # deserialize data into UpdateRegistrationFlowWithPasswordMethod
        try:
            instance.actual_instance = UpdateRegistrationFlowWithPasswordMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateRegistrationFlowWithOidcMethod
        try:
            instance.actual_instance = UpdateRegistrationFlowWithOidcMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateRegistrationFlowWithSamlMethod
        try:
            instance.actual_instance = UpdateRegistrationFlowWithSamlMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateRegistrationFlowWithWebAuthnMethod
        try:
            instance.actual_instance = UpdateRegistrationFlowWithWebAuthnMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateRegistrationFlowWithCodeMethod
        try:
            instance.actual_instance = UpdateRegistrationFlowWithCodeMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateRegistrationFlowWithPasskeyMethod
        try:
            instance.actual_instance = UpdateRegistrationFlowWithPasskeyMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateRegistrationFlowWithProfileMethod
        try:
            instance.actual_instance = UpdateRegistrationFlowWithProfileMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into UpdateRegistrationFlowBody with oneOf schemas: UpdateRegistrationFlowWithCodeMethod, UpdateRegistrationFlowWithOidcMethod, UpdateRegistrationFlowWithPasskeyMethod, UpdateRegistrationFlowWithPasswordMethod, UpdateRegistrationFlowWithProfileMethod, UpdateRegistrationFlowWithSamlMethod, UpdateRegistrationFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UpdateRegistrationFlowBody with oneOf schemas: UpdateRegistrationFlowWithCodeMethod, UpdateRegistrationFlowWithOidcMethod, UpdateRegistrationFlowWithPasskeyMethod, UpdateRegistrationFlowWithPasswordMethod, UpdateRegistrationFlowWithProfileMethod, UpdateRegistrationFlowWithSamlMethod, UpdateRegistrationFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], UpdateRegistrationFlowWithCodeMethod, UpdateRegistrationFlowWithOidcMethod, UpdateRegistrationFlowWithPasskeyMethod, UpdateRegistrationFlowWithPasswordMethod, UpdateRegistrationFlowWithProfileMethod, UpdateRegistrationFlowWithSamlMethod, UpdateRegistrationFlowWithWebAuthnMethod]]:
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


