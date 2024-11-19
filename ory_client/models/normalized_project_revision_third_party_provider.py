# coding: utf-8

"""
    Ory APIs

    # Introduction Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.  ## SDKs This document describes the APIs available in the Ory Network. The APIs are available as SDKs for the following languages:  | Language       | Download SDK                                                     | Documentation                                                                        | | -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ | | Dart           | [pub.dev](https://pub.dev/packages/ory_client)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/dart/README.md)       | | .NET           | [nuget.org](https://www.nuget.org/packages/Ory.Client/)          | [README](https://github.com/ory/sdk/blob/master/clients/client/dotnet/README.md)     | | Elixir         | [hex.pm](https://hex.pm/packages/ory_client)                     | [README](https://github.com/ory/sdk/blob/master/clients/client/elixir/README.md)     | | Go             | [github.com](https://github.com/ory/client-go)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/go/README.md)         | | Java           | [maven.org](https://search.maven.org/artifact/sh.ory/ory-client) | [README](https://github.com/ory/sdk/blob/master/clients/client/java/README.md)       | | JavaScript     | [npmjs.com](https://www.npmjs.com/package/@ory/client)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript/README.md) | | JavaScript (With fetch) | [npmjs.com](https://www.npmjs.com/package/@ory/client-fetch)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript-fetch/README.md) |  | PHP            | [packagist.org](https://packagist.org/packages/ory/client)       | [README](https://github.com/ory/sdk/blob/master/clients/client/php/README.md)        | | Python         | [pypi.org](https://pypi.org/project/ory-client/)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/python/README.md)     | | Ruby           | [rubygems.org](https://rubygems.org/gems/ory-client)             | [README](https://github.com/ory/sdk/blob/master/clients/client/ruby/README.md)       | | Rust           | [crates.io](https://crates.io/crates/ory-client)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/rust/README.md)       | 

    The version of the OpenAPI document: v1.15.12
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

class NormalizedProjectRevisionThirdPartyProvider(BaseModel):
    """
    NormalizedProjectRevisionThirdPartyProvider
    """ # noqa: E501
    additional_id_token_audiences: Optional[List[StrictStr]] = None
    apple_private_key: Optional[StrictStr] = None
    apple_private_key_id: Optional[StrictStr] = Field(default=None, description="Apple Private Key Identifier  Sign In with Apple Private Key Identifier needed for generating a JWT token for client secret")
    apple_team_id: Optional[StrictStr] = Field(default=None, description="Apple Developer Team ID  Apple Developer Team ID needed for generating a JWT token for client secret")
    auth_url: Optional[StrictStr] = Field(default=None, description="AuthURL is the authorize url, typically something like: https://example.org/oauth2/auth Should only be used when the OAuth2 / OpenID Connect server is not supporting OpenID Connect Discovery and when `provider` is set to `generic`.")
    azure_tenant: Optional[StrictStr] = Field(default=None, description="Tenant is the Azure AD Tenant to use for authentication, and must be set when `provider` is set to `microsoft`.  Can be either `common`, `organizations`, `consumers` for a multitenant application or a specific tenant like `8eaef023-2b34-4da1-9baa-8bc8c9d6a490` or `contoso.onmicrosoft.com`.")
    claims_source: Optional[StrictStr] = None
    client_id: Optional[StrictStr] = Field(default=None, description="ClientID is the application's Client ID.")
    client_secret: Optional[StrictStr] = None
    created_at: Optional[datetime] = Field(default=None, description="The Project's Revision Creation Date")
    id: Optional[StrictStr] = None
    issuer_url: Optional[StrictStr] = Field(default=None, description="IssuerURL is the OpenID Connect Server URL. You can leave this empty if `provider` is not set to `generic`. If set, neither `auth_url` nor `token_url` are required.")
    label: Optional[StrictStr] = Field(default=None, description="Label represents an optional label which can be used in the UI generation.")
    mapper_url: Optional[StrictStr] = Field(default=None, description="Mapper specifies the JSONNet code snippet which uses the OpenID Connect Provider's data (e.g. GitHub or Google profile information) to hydrate the identity's data.")
    organization_id: Optional[StrictStr] = None
    pkce: Optional[StrictStr] = Field(default=None, description="PKCE controls if the OpenID Connect OAuth2 flow should use PKCE (Proof Key for Code Exchange). Possible values are: `auto` (default), `never`, `force`. `auto`: PKCE is used if the provider supports it. Requires setting `issuer_url`. `never`: Disable PKCE entirely for this provider, even if the provider advertises support for it. `force`: Always use PKCE, even if the provider does not advertise support for it. OAuth2 flows will fail if the provider does not support PKCE. IMPORTANT: If you set this to `force`, you must whitelist a different return URL for your OAuth2 client in the provider's configuration. Instead of <base-url>/self-service/methods/oidc/callback/<provider>, you must use <base-url>/self-service/methods/oidc/callback (Note the missing <provider> path segment and no trailing slash).")
    project_revision_id: Optional[StrictStr] = Field(default=None, description="The Revision's ID this schema belongs to")
    provider: Optional[StrictStr] = Field(default=None, description="Provider is either \"generic\" for a generic OAuth 2.0 / OpenID Connect Provider or one of: generic google github gitlab microsoft discord slack facebook vk yandex apple")
    provider_id: Optional[StrictStr] = Field(default=None, description="ID is the provider's ID")
    requested_claims: Optional[Dict[str, Any]] = None
    scope: Optional[List[StrictStr]] = None
    state: Optional[StrictStr] = Field(default=None, description="State indicates the state of the provider  Only providers with state `enabled` will be used for authentication enabled ThirdPartyProviderStateEnabled disabled ThirdPartyProviderStateDisabled")
    subject_source: Optional[StrictStr] = None
    token_url: Optional[StrictStr] = Field(default=None, description="TokenURL is the token url, typically something like: https://example.org/oauth2/token  Should only be used when the OAuth2 / OpenID Connect server is not supporting OpenID Connect Discovery and when `provider` is set to `generic`.")
    updated_at: Optional[datetime] = Field(default=None, description="Last Time Project's Revision was Updated")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["additional_id_token_audiences", "apple_private_key", "apple_private_key_id", "apple_team_id", "auth_url", "azure_tenant", "claims_source", "client_id", "client_secret", "created_at", "id", "issuer_url", "label", "mapper_url", "organization_id", "pkce", "project_revision_id", "provider", "provider_id", "requested_claims", "scope", "state", "subject_source", "token_url", "updated_at"]

    @field_validator('pkce')
    def pkce_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['auto', 'never', 'force']):
            raise ValueError("must be one of enum values ('auto', 'never', 'force')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enabled', 'disabled']):
            raise ValueError("must be one of enum values ('enabled', 'disabled')")
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
        """Create an instance of NormalizedProjectRevisionThirdPartyProvider from a JSON string"""
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

        # set to None if apple_private_key (nullable) is None
        # and model_fields_set contains the field
        if self.apple_private_key is None and "apple_private_key" in self.model_fields_set:
            _dict['apple_private_key'] = None

        # set to None if claims_source (nullable) is None
        # and model_fields_set contains the field
        if self.claims_source is None and "claims_source" in self.model_fields_set:
            _dict['claims_source'] = None

        # set to None if client_secret (nullable) is None
        # and model_fields_set contains the field
        if self.client_secret is None and "client_secret" in self.model_fields_set:
            _dict['client_secret'] = None

        # set to None if organization_id (nullable) is None
        # and model_fields_set contains the field
        if self.organization_id is None and "organization_id" in self.model_fields_set:
            _dict['organization_id'] = None

        # set to None if pkce (nullable) is None
        # and model_fields_set contains the field
        if self.pkce is None and "pkce" in self.model_fields_set:
            _dict['pkce'] = None

        # set to None if subject_source (nullable) is None
        # and model_fields_set contains the field
        if self.subject_source is None and "subject_source" in self.model_fields_set:
            _dict['subject_source'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormalizedProjectRevisionThirdPartyProvider from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "additional_id_token_audiences": obj.get("additional_id_token_audiences"),
            "apple_private_key": obj.get("apple_private_key"),
            "apple_private_key_id": obj.get("apple_private_key_id"),
            "apple_team_id": obj.get("apple_team_id"),
            "auth_url": obj.get("auth_url"),
            "azure_tenant": obj.get("azure_tenant"),
            "claims_source": obj.get("claims_source"),
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "created_at": obj.get("created_at"),
            "id": obj.get("id"),
            "issuer_url": obj.get("issuer_url"),
            "label": obj.get("label"),
            "mapper_url": obj.get("mapper_url"),
            "organization_id": obj.get("organization_id"),
            "pkce": obj.get("pkce"),
            "project_revision_id": obj.get("project_revision_id"),
            "provider": obj.get("provider"),
            "provider_id": obj.get("provider_id"),
            "requested_claims": obj.get("requested_claims"),
            "scope": obj.get("scope"),
            "state": obj.get("state"),
            "subject_source": obj.get("subject_source"),
            "token_url": obj.get("token_url"),
            "updated_at": obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


