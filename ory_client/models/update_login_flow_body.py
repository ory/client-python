# coding: utf-8

"""
    Ory APIs

    # Introduction Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.  ## SDKs This document describes the APIs available in the Ory Network. The APIs are available as SDKs for the following languages:  | Language       | Download SDK                                                     | Documentation                                                                        | | -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ | | Dart           | [pub.dev](https://pub.dev/packages/ory_client)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/dart/README.md)       | | .NET           | [nuget.org](https://www.nuget.org/packages/Ory.Client/)          | [README](https://github.com/ory/sdk/blob/master/clients/client/dotnet/README.md)     | | Elixir         | [hex.pm](https://hex.pm/packages/ory_client)                     | [README](https://github.com/ory/sdk/blob/master/clients/client/elixir/README.md)     | | Go             | [github.com](https://github.com/ory/client-go)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/go/README.md)         | | Java           | [maven.org](https://search.maven.org/artifact/sh.ory/ory-client) | [README](https://github.com/ory/sdk/blob/master/clients/client/java/README.md)       | | JavaScript     | [npmjs.com](https://www.npmjs.com/package/@ory/client)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript/README.md) | | JavaScript (With fetch) | [npmjs.com](https://www.npmjs.com/package/@ory/client-fetch)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript-fetch/README.md) |  | PHP            | [packagist.org](https://packagist.org/packages/ory/client)       | [README](https://github.com/ory/sdk/blob/master/clients/client/php/README.md)        | | Python         | [pypi.org](https://pypi.org/project/ory-client/)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/python/README.md)     | | Ruby           | [rubygems.org](https://rubygems.org/gems/ory-client)             | [README](https://github.com/ory/sdk/blob/master/clients/client/ruby/README.md)       | | Rust           | [crates.io](https://crates.io/crates/ory-client)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/rust/README.md)       | 

    The version of the OpenAPI document: v1.16.3
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from ory_client.models.update_login_flow_with_code_method import UpdateLoginFlowWithCodeMethod
from ory_client.models.update_login_flow_with_identifier_first_method import UpdateLoginFlowWithIdentifierFirstMethod
from ory_client.models.update_login_flow_with_lookup_secret_method import UpdateLoginFlowWithLookupSecretMethod
from ory_client.models.update_login_flow_with_oidc_method import UpdateLoginFlowWithOidcMethod
from ory_client.models.update_login_flow_with_passkey_method import UpdateLoginFlowWithPasskeyMethod
from ory_client.models.update_login_flow_with_password_method import UpdateLoginFlowWithPasswordMethod
from ory_client.models.update_login_flow_with_totp_method import UpdateLoginFlowWithTotpMethod
from ory_client.models.update_login_flow_with_web_authn_method import UpdateLoginFlowWithWebAuthnMethod
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

UPDATELOGINFLOWBODY_ONE_OF_SCHEMAS = ["UpdateLoginFlowWithCodeMethod", "UpdateLoginFlowWithIdentifierFirstMethod", "UpdateLoginFlowWithLookupSecretMethod", "UpdateLoginFlowWithOidcMethod", "UpdateLoginFlowWithPasskeyMethod", "UpdateLoginFlowWithPasswordMethod", "UpdateLoginFlowWithTotpMethod", "UpdateLoginFlowWithWebAuthnMethod"]

class UpdateLoginFlowBody(BaseModel):
    """
    UpdateLoginFlowBody
    """
    # data type: UpdateLoginFlowWithPasswordMethod
    oneof_schema_1_validator: Optional[UpdateLoginFlowWithPasswordMethod] = None
    # data type: UpdateLoginFlowWithOidcMethod
    oneof_schema_2_validator: Optional[UpdateLoginFlowWithOidcMethod] = None
    # data type: UpdateLoginFlowWithTotpMethod
    oneof_schema_3_validator: Optional[UpdateLoginFlowWithTotpMethod] = None
    # data type: UpdateLoginFlowWithWebAuthnMethod
    oneof_schema_4_validator: Optional[UpdateLoginFlowWithWebAuthnMethod] = None
    # data type: UpdateLoginFlowWithLookupSecretMethod
    oneof_schema_5_validator: Optional[UpdateLoginFlowWithLookupSecretMethod] = None
    # data type: UpdateLoginFlowWithCodeMethod
    oneof_schema_6_validator: Optional[UpdateLoginFlowWithCodeMethod] = None
    # data type: UpdateLoginFlowWithPasskeyMethod
    oneof_schema_7_validator: Optional[UpdateLoginFlowWithPasskeyMethod] = None
    # data type: UpdateLoginFlowWithIdentifierFirstMethod
    oneof_schema_8_validator: Optional[UpdateLoginFlowWithIdentifierFirstMethod] = None
    actual_instance: Optional[Union[UpdateLoginFlowWithCodeMethod, UpdateLoginFlowWithIdentifierFirstMethod, UpdateLoginFlowWithLookupSecretMethod, UpdateLoginFlowWithOidcMethod, UpdateLoginFlowWithPasskeyMethod, UpdateLoginFlowWithPasswordMethod, UpdateLoginFlowWithTotpMethod, UpdateLoginFlowWithWebAuthnMethod]] = None
    one_of_schemas: Set[str] = { "UpdateLoginFlowWithCodeMethod", "UpdateLoginFlowWithIdentifierFirstMethod", "UpdateLoginFlowWithLookupSecretMethod", "UpdateLoginFlowWithOidcMethod", "UpdateLoginFlowWithPasskeyMethod", "UpdateLoginFlowWithPasswordMethod", "UpdateLoginFlowWithTotpMethod", "UpdateLoginFlowWithWebAuthnMethod" }

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
        instance = UpdateLoginFlowBody.model_construct()
        error_messages = []
        match = 0
        # validate data type: UpdateLoginFlowWithPasswordMethod
        if not isinstance(v, UpdateLoginFlowWithPasswordMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateLoginFlowWithPasswordMethod`")
        else:
            match += 1
        # validate data type: UpdateLoginFlowWithOidcMethod
        if not isinstance(v, UpdateLoginFlowWithOidcMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateLoginFlowWithOidcMethod`")
        else:
            match += 1
        # validate data type: UpdateLoginFlowWithTotpMethod
        if not isinstance(v, UpdateLoginFlowWithTotpMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateLoginFlowWithTotpMethod`")
        else:
            match += 1
        # validate data type: UpdateLoginFlowWithWebAuthnMethod
        if not isinstance(v, UpdateLoginFlowWithWebAuthnMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateLoginFlowWithWebAuthnMethod`")
        else:
            match += 1
        # validate data type: UpdateLoginFlowWithLookupSecretMethod
        if not isinstance(v, UpdateLoginFlowWithLookupSecretMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateLoginFlowWithLookupSecretMethod`")
        else:
            match += 1
        # validate data type: UpdateLoginFlowWithCodeMethod
        if not isinstance(v, UpdateLoginFlowWithCodeMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateLoginFlowWithCodeMethod`")
        else:
            match += 1
        # validate data type: UpdateLoginFlowWithPasskeyMethod
        if not isinstance(v, UpdateLoginFlowWithPasskeyMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateLoginFlowWithPasskeyMethod`")
        else:
            match += 1
        # validate data type: UpdateLoginFlowWithIdentifierFirstMethod
        if not isinstance(v, UpdateLoginFlowWithIdentifierFirstMethod):
            error_messages.append(f"Error! Input type `{type(v)}` is not `UpdateLoginFlowWithIdentifierFirstMethod`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in UpdateLoginFlowBody with oneOf schemas: UpdateLoginFlowWithCodeMethod, UpdateLoginFlowWithIdentifierFirstMethod, UpdateLoginFlowWithLookupSecretMethod, UpdateLoginFlowWithOidcMethod, UpdateLoginFlowWithPasskeyMethod, UpdateLoginFlowWithPasswordMethod, UpdateLoginFlowWithTotpMethod, UpdateLoginFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in UpdateLoginFlowBody with oneOf schemas: UpdateLoginFlowWithCodeMethod, UpdateLoginFlowWithIdentifierFirstMethod, UpdateLoginFlowWithLookupSecretMethod, UpdateLoginFlowWithOidcMethod, UpdateLoginFlowWithPasskeyMethod, UpdateLoginFlowWithPasswordMethod, UpdateLoginFlowWithTotpMethod, UpdateLoginFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
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

        # check if data type is `UpdateLoginFlowWithCodeMethod`
        if _data_type == "code":
            instance.actual_instance = UpdateLoginFlowWithCodeMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithIdentifierFirstMethod`
        if _data_type == "identifier_first":
            instance.actual_instance = UpdateLoginFlowWithIdentifierFirstMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithLookupSecretMethod`
        if _data_type == "lookup_secret":
            instance.actual_instance = UpdateLoginFlowWithLookupSecretMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithOidcMethod`
        if _data_type == "oidc":
            instance.actual_instance = UpdateLoginFlowWithOidcMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithPasskeyMethod`
        if _data_type == "passkey":
            instance.actual_instance = UpdateLoginFlowWithPasskeyMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithPasswordMethod`
        if _data_type == "password":
            instance.actual_instance = UpdateLoginFlowWithPasswordMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithTotpMethod`
        if _data_type == "totp":
            instance.actual_instance = UpdateLoginFlowWithTotpMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithWebAuthnMethod`
        if _data_type == "webauthn":
            instance.actual_instance = UpdateLoginFlowWithWebAuthnMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithCodeMethod`
        if _data_type == "updateLoginFlowWithCodeMethod":
            instance.actual_instance = UpdateLoginFlowWithCodeMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithIdentifierFirstMethod`
        if _data_type == "updateLoginFlowWithIdentifierFirstMethod":
            instance.actual_instance = UpdateLoginFlowWithIdentifierFirstMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithLookupSecretMethod`
        if _data_type == "updateLoginFlowWithLookupSecretMethod":
            instance.actual_instance = UpdateLoginFlowWithLookupSecretMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithOidcMethod`
        if _data_type == "updateLoginFlowWithOidcMethod":
            instance.actual_instance = UpdateLoginFlowWithOidcMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithPasskeyMethod`
        if _data_type == "updateLoginFlowWithPasskeyMethod":
            instance.actual_instance = UpdateLoginFlowWithPasskeyMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithPasswordMethod`
        if _data_type == "updateLoginFlowWithPasswordMethod":
            instance.actual_instance = UpdateLoginFlowWithPasswordMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithTotpMethod`
        if _data_type == "updateLoginFlowWithTotpMethod":
            instance.actual_instance = UpdateLoginFlowWithTotpMethod.from_json(json_str)
            return instance

        # check if data type is `UpdateLoginFlowWithWebAuthnMethod`
        if _data_type == "updateLoginFlowWithWebAuthnMethod":
            instance.actual_instance = UpdateLoginFlowWithWebAuthnMethod.from_json(json_str)
            return instance

        # deserialize data into UpdateLoginFlowWithPasswordMethod
        try:
            instance.actual_instance = UpdateLoginFlowWithPasswordMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateLoginFlowWithOidcMethod
        try:
            instance.actual_instance = UpdateLoginFlowWithOidcMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateLoginFlowWithTotpMethod
        try:
            instance.actual_instance = UpdateLoginFlowWithTotpMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateLoginFlowWithWebAuthnMethod
        try:
            instance.actual_instance = UpdateLoginFlowWithWebAuthnMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateLoginFlowWithLookupSecretMethod
        try:
            instance.actual_instance = UpdateLoginFlowWithLookupSecretMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateLoginFlowWithCodeMethod
        try:
            instance.actual_instance = UpdateLoginFlowWithCodeMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateLoginFlowWithPasskeyMethod
        try:
            instance.actual_instance = UpdateLoginFlowWithPasskeyMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into UpdateLoginFlowWithIdentifierFirstMethod
        try:
            instance.actual_instance = UpdateLoginFlowWithIdentifierFirstMethod.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into UpdateLoginFlowBody with oneOf schemas: UpdateLoginFlowWithCodeMethod, UpdateLoginFlowWithIdentifierFirstMethod, UpdateLoginFlowWithLookupSecretMethod, UpdateLoginFlowWithOidcMethod, UpdateLoginFlowWithPasskeyMethod, UpdateLoginFlowWithPasswordMethod, UpdateLoginFlowWithTotpMethod, UpdateLoginFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into UpdateLoginFlowBody with oneOf schemas: UpdateLoginFlowWithCodeMethod, UpdateLoginFlowWithIdentifierFirstMethod, UpdateLoginFlowWithLookupSecretMethod, UpdateLoginFlowWithOidcMethod, UpdateLoginFlowWithPasskeyMethod, UpdateLoginFlowWithPasswordMethod, UpdateLoginFlowWithTotpMethod, UpdateLoginFlowWithWebAuthnMethod. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], UpdateLoginFlowWithCodeMethod, UpdateLoginFlowWithIdentifierFirstMethod, UpdateLoginFlowWithLookupSecretMethod, UpdateLoginFlowWithOidcMethod, UpdateLoginFlowWithPasskeyMethod, UpdateLoginFlowWithPasswordMethod, UpdateLoginFlowWithTotpMethod, UpdateLoginFlowWithWebAuthnMethod]]:
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


