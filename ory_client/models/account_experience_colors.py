# coding: utf-8

"""
    Ory APIs

    # Introduction Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers.  ## SDKs This document describes the APIs available in the Ory Network. The APIs are available as SDKs for the following languages:  | Language       | Download SDK                                                     | Documentation                                                                        | | -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------ | | Dart           | [pub.dev](https://pub.dev/packages/ory_client)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/dart/README.md)       | | .NET           | [nuget.org](https://www.nuget.org/packages/Ory.Client/)          | [README](https://github.com/ory/sdk/blob/master/clients/client/dotnet/README.md)     | | Elixir         | [hex.pm](https://hex.pm/packages/ory_client)                     | [README](https://github.com/ory/sdk/blob/master/clients/client/elixir/README.md)     | | Go             | [github.com](https://github.com/ory/client-go)                   | [README](https://github.com/ory/sdk/blob/master/clients/client/go/README.md)         | | Java           | [maven.org](https://search.maven.org/artifact/sh.ory/ory-client) | [README](https://github.com/ory/sdk/blob/master/clients/client/java/README.md)       | | JavaScript     | [npmjs.com](https://www.npmjs.com/package/@ory/client)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript/README.md) | | JavaScript (With fetch) | [npmjs.com](https://www.npmjs.com/package/@ory/client-fetch)           | [README](https://github.com/ory/sdk/blob/master/clients/client/typescript-fetch/README.md) |  | PHP            | [packagist.org](https://packagist.org/packages/ory/client)       | [README](https://github.com/ory/sdk/blob/master/clients/client/php/README.md)        | | Python         | [pypi.org](https://pypi.org/project/ory-client/)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/python/README.md)     | | Ruby           | [rubygems.org](https://rubygems.org/gems/ory-client)             | [README](https://github.com/ory/sdk/blob/master/clients/client/ruby/README.md)       | | Rust           | [crates.io](https://crates.io/crates/ory-client)                 | [README](https://github.com/ory/sdk/blob/master/clients/client/rust/README.md)       | 

    The version of the OpenAPI document: v1.20.0
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AccountExperienceColors(BaseModel):
    """
    AccountExperienceColors
    """ # noqa: E501
    brand_100: Optional[StrictStr] = Field(default=None, alias="brand-100")
    brand_200: Optional[StrictStr] = Field(default=None, alias="brand-200")
    brand_300: Optional[StrictStr] = Field(default=None, alias="brand-300")
    brand_400: Optional[StrictStr] = Field(default=None, alias="brand-400")
    brand_50: Optional[StrictStr] = Field(default=None, alias="brand-50")
    brand_500: Optional[StrictStr] = Field(default=None, alias="brand-500")
    brand_600: Optional[StrictStr] = Field(default=None, alias="brand-600")
    brand_700: Optional[StrictStr] = Field(default=None, alias="brand-700")
    brand_800: Optional[StrictStr] = Field(default=None, alias="brand-800")
    brand_900: Optional[StrictStr] = Field(default=None, alias="brand-900")
    brand_950: Optional[StrictStr] = Field(default=None, alias="brand-950")
    button_identifier_background_default: Optional[StrictStr] = Field(default=None, alias="button-identifier-background-default")
    button_identifier_background_hover: Optional[StrictStr] = Field(default=None, alias="button-identifier-background-hover")
    button_identifier_border_border_default: Optional[StrictStr] = Field(default=None, alias="button-identifier-border-border-default")
    button_identifier_border_border_hover: Optional[StrictStr] = Field(default=None, alias="button-identifier-border-border-hover")
    button_identifier_foreground_default: Optional[StrictStr] = Field(default=None, alias="button-identifier-foreground-default")
    button_identifier_foreground_hover: Optional[StrictStr] = Field(default=None, alias="button-identifier-foreground-hover")
    button_link_brand_brand: Optional[StrictStr] = Field(default=None, alias="button-link-brand-brand")
    button_link_brand_brand_hover: Optional[StrictStr] = Field(default=None, alias="button-link-brand-brand-hover")
    button_link_default_primary: Optional[StrictStr] = Field(default=None, alias="button-link-default-primary")
    button_link_default_primary_hover: Optional[StrictStr] = Field(default=None, alias="button-link-default-primary-hover")
    button_link_default_secondary: Optional[StrictStr] = Field(default=None, alias="button-link-default-secondary")
    button_link_default_secondary_hover: Optional[StrictStr] = Field(default=None, alias="button-link-default-secondary-hover")
    button_link_disabled_disabled: Optional[StrictStr] = Field(default=None, alias="button-link-disabled-disabled")
    button_primary_background_default: Optional[StrictStr] = Field(default=None, alias="button-primary-background-default")
    button_primary_background_disabled: Optional[StrictStr] = Field(default=None, alias="button-primary-background-disabled")
    button_primary_background_hover: Optional[StrictStr] = Field(default=None, alias="button-primary-background-hover")
    button_primary_border_default: Optional[StrictStr] = Field(default=None, alias="button-primary-border-default")
    button_primary_border_disabled: Optional[StrictStr] = Field(default=None, alias="button-primary-border-disabled")
    button_primary_border_hover: Optional[StrictStr] = Field(default=None, alias="button-primary-border-hover")
    button_primary_foreground_default: Optional[StrictStr] = Field(default=None, alias="button-primary-foreground-default")
    button_primary_foreground_disabled: Optional[StrictStr] = Field(default=None, alias="button-primary-foreground-disabled")
    button_primary_foreground_hover: Optional[StrictStr] = Field(default=None, alias="button-primary-foreground-hover")
    button_secondary_background_default: Optional[StrictStr] = Field(default=None, alias="button-secondary-background-default")
    button_secondary_background_disabled: Optional[StrictStr] = Field(default=None, alias="button-secondary-background-disabled")
    button_secondary_background_hover: Optional[StrictStr] = Field(default=None, alias="button-secondary-background-hover")
    button_secondary_border_default: Optional[StrictStr] = Field(default=None, alias="button-secondary-border-default")
    button_secondary_border_disabled: Optional[StrictStr] = Field(default=None, alias="button-secondary-border-disabled")
    button_secondary_border_hover: Optional[StrictStr] = Field(default=None, alias="button-secondary-border-hover")
    button_secondary_foreground_default: Optional[StrictStr] = Field(default=None, alias="button-secondary-foreground-default")
    button_secondary_foreground_disabled: Optional[StrictStr] = Field(default=None, alias="button-secondary-foreground-disabled")
    button_secondary_foreground_hover: Optional[StrictStr] = Field(default=None, alias="button-secondary-foreground-hover")
    button_social_background_default: Optional[StrictStr] = Field(default=None, alias="button-social-background-default")
    button_social_background_disabled: Optional[StrictStr] = Field(default=None, alias="button-social-background-disabled")
    button_social_background_generic_provider: Optional[StrictStr] = Field(default=None, alias="button-social-background-generic-provider")
    button_social_background_hover: Optional[StrictStr] = Field(default=None, alias="button-social-background-hover")
    button_social_border_default: Optional[StrictStr] = Field(default=None, alias="button-social-border-default")
    button_social_border_disabled: Optional[StrictStr] = Field(default=None, alias="button-social-border-disabled")
    button_social_border_generic_provider: Optional[StrictStr] = Field(default=None, alias="button-social-border-generic-provider")
    button_social_border_hover: Optional[StrictStr] = Field(default=None, alias="button-social-border-hover")
    button_social_foreground_default: Optional[StrictStr] = Field(default=None, alias="button-social-foreground-default")
    button_social_foreground_disabled: Optional[StrictStr] = Field(default=None, alias="button-social-foreground-disabled")
    button_social_foreground_generic_provider: Optional[StrictStr] = Field(default=None, alias="button-social-foreground-generic-provider")
    button_social_foreground_hover: Optional[StrictStr] = Field(default=None, alias="button-social-foreground-hover")
    checkbox_background_checked: Optional[StrictStr] = Field(default=None, alias="checkbox-background-checked")
    checkbox_background_default: Optional[StrictStr] = Field(default=None, alias="checkbox-background-default")
    checkbox_border_checkbox_border_checked: Optional[StrictStr] = Field(default=None, alias="checkbox-border-checkbox-border-checked")
    checkbox_border_checkbox_border_default: Optional[StrictStr] = Field(default=None, alias="checkbox-border-checkbox-border-default")
    checkbox_foreground_checked: Optional[StrictStr] = Field(default=None, alias="checkbox-foreground-checked")
    checkbox_foreground_default: Optional[StrictStr] = Field(default=None, alias="checkbox-foreground-default")
    form_background_default: Optional[StrictStr] = Field(default=None, alias="form-background-default")
    form_border_default: Optional[StrictStr] = Field(default=None, alias="form-border-default")
    input_background_default: Optional[StrictStr] = Field(default=None, alias="input-background-default")
    input_background_disabled: Optional[StrictStr] = Field(default=None, alias="input-background-disabled")
    input_background_hover: Optional[StrictStr] = Field(default=None, alias="input-background-hover")
    input_border_default: Optional[StrictStr] = Field(default=None, alias="input-border-default")
    input_border_disabled: Optional[StrictStr] = Field(default=None, alias="input-border-disabled")
    input_border_focus: Optional[StrictStr] = Field(default=None, alias="input-border-focus")
    input_border_hover: Optional[StrictStr] = Field(default=None, alias="input-border-hover")
    input_foreground_disabled: Optional[StrictStr] = Field(default=None, alias="input-foreground-disabled")
    input_foreground_primary: Optional[StrictStr] = Field(default=None, alias="input-foreground-primary")
    input_foreground_secondary: Optional[StrictStr] = Field(default=None, alias="input-foreground-secondary")
    input_foreground_tertiary: Optional[StrictStr] = Field(default=None, alias="input-foreground-tertiary")
    interface_background_brand_primary: Optional[StrictStr] = Field(default=None, alias="interface-background-brand-primary")
    interface_background_brand_primary_hover: Optional[StrictStr] = Field(default=None, alias="interface-background-brand-primary-hover")
    interface_background_brand_secondary: Optional[StrictStr] = Field(default=None, alias="interface-background-brand-secondary")
    interface_background_brand_secondary_hover: Optional[StrictStr] = Field(default=None, alias="interface-background-brand-secondary-hover")
    interface_background_default_inverted: Optional[StrictStr] = Field(default=None, alias="interface-background-default-inverted")
    interface_background_default_inverted_hover: Optional[StrictStr] = Field(default=None, alias="interface-background-default-inverted-hover")
    interface_background_default_none: Optional[StrictStr] = Field(default=None, alias="interface-background-default-none")
    interface_background_default_primary: Optional[StrictStr] = Field(default=None, alias="interface-background-default-primary")
    interface_background_default_primary_hover: Optional[StrictStr] = Field(default=None, alias="interface-background-default-primary-hover")
    interface_background_default_secondary: Optional[StrictStr] = Field(default=None, alias="interface-background-default-secondary")
    interface_background_default_secondary_hover: Optional[StrictStr] = Field(default=None, alias="interface-background-default-secondary-hover")
    interface_background_default_tertiary: Optional[StrictStr] = Field(default=None, alias="interface-background-default-tertiary")
    interface_background_default_tertiary_hover: Optional[StrictStr] = Field(default=None, alias="interface-background-default-tertiary-hover")
    interface_background_disabled_disabled: Optional[StrictStr] = Field(default=None, alias="interface-background-disabled-disabled")
    interface_background_validation_danger: Optional[StrictStr] = Field(default=None, alias="interface-background-validation-danger")
    interface_background_validation_success: Optional[StrictStr] = Field(default=None, alias="interface-background-validation-success")
    interface_background_validation_warning: Optional[StrictStr] = Field(default=None, alias="interface-background-validation-warning")
    interface_border_brand_brand: Optional[StrictStr] = Field(default=None, alias="interface-border-brand-brand")
    interface_border_default_inverted: Optional[StrictStr] = Field(default=None, alias="interface-border-default-inverted")
    interface_border_default_none: Optional[StrictStr] = Field(default=None, alias="interface-border-default-none")
    interface_border_default_primary: Optional[StrictStr] = Field(default=None, alias="interface-border-default-primary")
    interface_border_disabled_disabled: Optional[StrictStr] = Field(default=None, alias="interface-border-disabled-disabled")
    interface_border_validation_danger: Optional[StrictStr] = Field(default=None, alias="interface-border-validation-danger")
    interface_border_validation_success: Optional[StrictStr] = Field(default=None, alias="interface-border-validation-success")
    interface_border_validation_warning: Optional[StrictStr] = Field(default=None, alias="interface-border-validation-warning")
    interface_foreground_brand_on_primary: Optional[StrictStr] = Field(default=None, alias="interface-foreground-brand-on-primary")
    interface_foreground_brand_on_secondary: Optional[StrictStr] = Field(default=None, alias="interface-foreground-brand-on-secondary")
    interface_foreground_brand_primary: Optional[StrictStr] = Field(default=None, alias="interface-foreground-brand-primary")
    interface_foreground_brand_secondary: Optional[StrictStr] = Field(default=None, alias="interface-foreground-brand-secondary")
    interface_foreground_default_inverted: Optional[StrictStr] = Field(default=None, alias="interface-foreground-default-inverted")
    interface_foreground_default_primary: Optional[StrictStr] = Field(default=None, alias="interface-foreground-default-primary")
    interface_foreground_default_secondary: Optional[StrictStr] = Field(default=None, alias="interface-foreground-default-secondary")
    interface_foreground_default_tertiary: Optional[StrictStr] = Field(default=None, alias="interface-foreground-default-tertiary")
    interface_foreground_disabled_disabled: Optional[StrictStr] = Field(default=None, alias="interface-foreground-disabled-disabled")
    interface_foreground_disabled_on_disabled: Optional[StrictStr] = Field(default=None, alias="interface-foreground-disabled-on-disabled")
    interface_foreground_validation_danger: Optional[StrictStr] = Field(default=None, alias="interface-foreground-validation-danger")
    interface_foreground_validation_success: Optional[StrictStr] = Field(default=None, alias="interface-foreground-validation-success")
    interface_foreground_validation_warning: Optional[StrictStr] = Field(default=None, alias="interface-foreground-validation-warning")
    ory_background_default: Optional[StrictStr] = Field(default=None, alias="ory-background-default")
    ory_border_default: Optional[StrictStr] = Field(default=None, alias="ory-border-default")
    ory_foreground_default: Optional[StrictStr] = Field(default=None, alias="ory-foreground-default")
    radio_background_checked: Optional[StrictStr] = Field(default=None, alias="radio-background-checked")
    radio_background_default: Optional[StrictStr] = Field(default=None, alias="radio-background-default")
    radio_border_checked: Optional[StrictStr] = Field(default=None, alias="radio-border-checked")
    radio_border_default: Optional[StrictStr] = Field(default=None, alias="radio-border-default")
    radio_foreground_checked: Optional[StrictStr] = Field(default=None, alias="radio-foreground-checked")
    radio_foreground_default: Optional[StrictStr] = Field(default=None, alias="radio-foreground-default")
    toggle_background_checked: Optional[StrictStr] = Field(default=None, alias="toggle-background-checked")
    toggle_background_default: Optional[StrictStr] = Field(default=None, alias="toggle-background-default")
    toggle_border_checked: Optional[StrictStr] = Field(default=None, alias="toggle-border-checked")
    toggle_border_default: Optional[StrictStr] = Field(default=None, alias="toggle-border-default")
    toggle_foreground_checked: Optional[StrictStr] = Field(default=None, alias="toggle-foreground-checked")
    toggle_foreground_default: Optional[StrictStr] = Field(default=None, alias="toggle-foreground-default")
    ui_100: Optional[StrictStr] = Field(default=None, alias="ui-100")
    ui_200: Optional[StrictStr] = Field(default=None, alias="ui-200")
    ui_300: Optional[StrictStr] = Field(default=None, alias="ui-300")
    ui_400: Optional[StrictStr] = Field(default=None, alias="ui-400")
    ui_50: Optional[StrictStr] = Field(default=None, alias="ui-50")
    ui_500: Optional[StrictStr] = Field(default=None, alias="ui-500")
    ui_600: Optional[StrictStr] = Field(default=None, alias="ui-600")
    ui_700: Optional[StrictStr] = Field(default=None, alias="ui-700")
    ui_800: Optional[StrictStr] = Field(default=None, alias="ui-800")
    ui_900: Optional[StrictStr] = Field(default=None, alias="ui-900")
    ui_950: Optional[StrictStr] = Field(default=None, alias="ui-950")
    ui_black: Optional[StrictStr] = Field(default=None, alias="ui-black")
    ui_danger: Optional[StrictStr] = Field(default=None, alias="ui-danger")
    ui_success: Optional[StrictStr] = Field(default=None, alias="ui-success")
    ui_transparent: Optional[StrictStr] = Field(default=None, alias="ui-transparent")
    ui_warning: Optional[StrictStr] = Field(default=None, alias="ui-warning")
    ui_white: Optional[StrictStr] = Field(default=None, alias="ui-white")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["brand-100", "brand-200", "brand-300", "brand-400", "brand-50", "brand-500", "brand-600", "brand-700", "brand-800", "brand-900", "brand-950", "button-identifier-background-default", "button-identifier-background-hover", "button-identifier-border-border-default", "button-identifier-border-border-hover", "button-identifier-foreground-default", "button-identifier-foreground-hover", "button-link-brand-brand", "button-link-brand-brand-hover", "button-link-default-primary", "button-link-default-primary-hover", "button-link-default-secondary", "button-link-default-secondary-hover", "button-link-disabled-disabled", "button-primary-background-default", "button-primary-background-disabled", "button-primary-background-hover", "button-primary-border-default", "button-primary-border-disabled", "button-primary-border-hover", "button-primary-foreground-default", "button-primary-foreground-disabled", "button-primary-foreground-hover", "button-secondary-background-default", "button-secondary-background-disabled", "button-secondary-background-hover", "button-secondary-border-default", "button-secondary-border-disabled", "button-secondary-border-hover", "button-secondary-foreground-default", "button-secondary-foreground-disabled", "button-secondary-foreground-hover", "button-social-background-default", "button-social-background-disabled", "button-social-background-generic-provider", "button-social-background-hover", "button-social-border-default", "button-social-border-disabled", "button-social-border-generic-provider", "button-social-border-hover", "button-social-foreground-default", "button-social-foreground-disabled", "button-social-foreground-generic-provider", "button-social-foreground-hover", "checkbox-background-checked", "checkbox-background-default", "checkbox-border-checkbox-border-checked", "checkbox-border-checkbox-border-default", "checkbox-foreground-checked", "checkbox-foreground-default", "form-background-default", "form-border-default", "input-background-default", "input-background-disabled", "input-background-hover", "input-border-default", "input-border-disabled", "input-border-focus", "input-border-hover", "input-foreground-disabled", "input-foreground-primary", "input-foreground-secondary", "input-foreground-tertiary", "interface-background-brand-primary", "interface-background-brand-primary-hover", "interface-background-brand-secondary", "interface-background-brand-secondary-hover", "interface-background-default-inverted", "interface-background-default-inverted-hover", "interface-background-default-none", "interface-background-default-primary", "interface-background-default-primary-hover", "interface-background-default-secondary", "interface-background-default-secondary-hover", "interface-background-default-tertiary", "interface-background-default-tertiary-hover", "interface-background-disabled-disabled", "interface-background-validation-danger", "interface-background-validation-success", "interface-background-validation-warning", "interface-border-brand-brand", "interface-border-default-inverted", "interface-border-default-none", "interface-border-default-primary", "interface-border-disabled-disabled", "interface-border-validation-danger", "interface-border-validation-success", "interface-border-validation-warning", "interface-foreground-brand-on-primary", "interface-foreground-brand-on-secondary", "interface-foreground-brand-primary", "interface-foreground-brand-secondary", "interface-foreground-default-inverted", "interface-foreground-default-primary", "interface-foreground-default-secondary", "interface-foreground-default-tertiary", "interface-foreground-disabled-disabled", "interface-foreground-disabled-on-disabled", "interface-foreground-validation-danger", "interface-foreground-validation-success", "interface-foreground-validation-warning", "ory-background-default", "ory-border-default", "ory-foreground-default", "radio-background-checked", "radio-background-default", "radio-border-checked", "radio-border-default", "radio-foreground-checked", "radio-foreground-default", "toggle-background-checked", "toggle-background-default", "toggle-border-checked", "toggle-border-default", "toggle-foreground-checked", "toggle-foreground-default", "ui-100", "ui-200", "ui-300", "ui-400", "ui-50", "ui-500", "ui-600", "ui-700", "ui-800", "ui-900", "ui-950", "ui-black", "ui-danger", "ui-success", "ui-transparent", "ui-warning", "ui-white"]

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
        """Create an instance of AccountExperienceColors from a JSON string"""
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
        """Create an instance of AccountExperienceColors from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "brand-100": obj.get("brand-100"),
            "brand-200": obj.get("brand-200"),
            "brand-300": obj.get("brand-300"),
            "brand-400": obj.get("brand-400"),
            "brand-50": obj.get("brand-50"),
            "brand-500": obj.get("brand-500"),
            "brand-600": obj.get("brand-600"),
            "brand-700": obj.get("brand-700"),
            "brand-800": obj.get("brand-800"),
            "brand-900": obj.get("brand-900"),
            "brand-950": obj.get("brand-950"),
            "button-identifier-background-default": obj.get("button-identifier-background-default"),
            "button-identifier-background-hover": obj.get("button-identifier-background-hover"),
            "button-identifier-border-border-default": obj.get("button-identifier-border-border-default"),
            "button-identifier-border-border-hover": obj.get("button-identifier-border-border-hover"),
            "button-identifier-foreground-default": obj.get("button-identifier-foreground-default"),
            "button-identifier-foreground-hover": obj.get("button-identifier-foreground-hover"),
            "button-link-brand-brand": obj.get("button-link-brand-brand"),
            "button-link-brand-brand-hover": obj.get("button-link-brand-brand-hover"),
            "button-link-default-primary": obj.get("button-link-default-primary"),
            "button-link-default-primary-hover": obj.get("button-link-default-primary-hover"),
            "button-link-default-secondary": obj.get("button-link-default-secondary"),
            "button-link-default-secondary-hover": obj.get("button-link-default-secondary-hover"),
            "button-link-disabled-disabled": obj.get("button-link-disabled-disabled"),
            "button-primary-background-default": obj.get("button-primary-background-default"),
            "button-primary-background-disabled": obj.get("button-primary-background-disabled"),
            "button-primary-background-hover": obj.get("button-primary-background-hover"),
            "button-primary-border-default": obj.get("button-primary-border-default"),
            "button-primary-border-disabled": obj.get("button-primary-border-disabled"),
            "button-primary-border-hover": obj.get("button-primary-border-hover"),
            "button-primary-foreground-default": obj.get("button-primary-foreground-default"),
            "button-primary-foreground-disabled": obj.get("button-primary-foreground-disabled"),
            "button-primary-foreground-hover": obj.get("button-primary-foreground-hover"),
            "button-secondary-background-default": obj.get("button-secondary-background-default"),
            "button-secondary-background-disabled": obj.get("button-secondary-background-disabled"),
            "button-secondary-background-hover": obj.get("button-secondary-background-hover"),
            "button-secondary-border-default": obj.get("button-secondary-border-default"),
            "button-secondary-border-disabled": obj.get("button-secondary-border-disabled"),
            "button-secondary-border-hover": obj.get("button-secondary-border-hover"),
            "button-secondary-foreground-default": obj.get("button-secondary-foreground-default"),
            "button-secondary-foreground-disabled": obj.get("button-secondary-foreground-disabled"),
            "button-secondary-foreground-hover": obj.get("button-secondary-foreground-hover"),
            "button-social-background-default": obj.get("button-social-background-default"),
            "button-social-background-disabled": obj.get("button-social-background-disabled"),
            "button-social-background-generic-provider": obj.get("button-social-background-generic-provider"),
            "button-social-background-hover": obj.get("button-social-background-hover"),
            "button-social-border-default": obj.get("button-social-border-default"),
            "button-social-border-disabled": obj.get("button-social-border-disabled"),
            "button-social-border-generic-provider": obj.get("button-social-border-generic-provider"),
            "button-social-border-hover": obj.get("button-social-border-hover"),
            "button-social-foreground-default": obj.get("button-social-foreground-default"),
            "button-social-foreground-disabled": obj.get("button-social-foreground-disabled"),
            "button-social-foreground-generic-provider": obj.get("button-social-foreground-generic-provider"),
            "button-social-foreground-hover": obj.get("button-social-foreground-hover"),
            "checkbox-background-checked": obj.get("checkbox-background-checked"),
            "checkbox-background-default": obj.get("checkbox-background-default"),
            "checkbox-border-checkbox-border-checked": obj.get("checkbox-border-checkbox-border-checked"),
            "checkbox-border-checkbox-border-default": obj.get("checkbox-border-checkbox-border-default"),
            "checkbox-foreground-checked": obj.get("checkbox-foreground-checked"),
            "checkbox-foreground-default": obj.get("checkbox-foreground-default"),
            "form-background-default": obj.get("form-background-default"),
            "form-border-default": obj.get("form-border-default"),
            "input-background-default": obj.get("input-background-default"),
            "input-background-disabled": obj.get("input-background-disabled"),
            "input-background-hover": obj.get("input-background-hover"),
            "input-border-default": obj.get("input-border-default"),
            "input-border-disabled": obj.get("input-border-disabled"),
            "input-border-focus": obj.get("input-border-focus"),
            "input-border-hover": obj.get("input-border-hover"),
            "input-foreground-disabled": obj.get("input-foreground-disabled"),
            "input-foreground-primary": obj.get("input-foreground-primary"),
            "input-foreground-secondary": obj.get("input-foreground-secondary"),
            "input-foreground-tertiary": obj.get("input-foreground-tertiary"),
            "interface-background-brand-primary": obj.get("interface-background-brand-primary"),
            "interface-background-brand-primary-hover": obj.get("interface-background-brand-primary-hover"),
            "interface-background-brand-secondary": obj.get("interface-background-brand-secondary"),
            "interface-background-brand-secondary-hover": obj.get("interface-background-brand-secondary-hover"),
            "interface-background-default-inverted": obj.get("interface-background-default-inverted"),
            "interface-background-default-inverted-hover": obj.get("interface-background-default-inverted-hover"),
            "interface-background-default-none": obj.get("interface-background-default-none"),
            "interface-background-default-primary": obj.get("interface-background-default-primary"),
            "interface-background-default-primary-hover": obj.get("interface-background-default-primary-hover"),
            "interface-background-default-secondary": obj.get("interface-background-default-secondary"),
            "interface-background-default-secondary-hover": obj.get("interface-background-default-secondary-hover"),
            "interface-background-default-tertiary": obj.get("interface-background-default-tertiary"),
            "interface-background-default-tertiary-hover": obj.get("interface-background-default-tertiary-hover"),
            "interface-background-disabled-disabled": obj.get("interface-background-disabled-disabled"),
            "interface-background-validation-danger": obj.get("interface-background-validation-danger"),
            "interface-background-validation-success": obj.get("interface-background-validation-success"),
            "interface-background-validation-warning": obj.get("interface-background-validation-warning"),
            "interface-border-brand-brand": obj.get("interface-border-brand-brand"),
            "interface-border-default-inverted": obj.get("interface-border-default-inverted"),
            "interface-border-default-none": obj.get("interface-border-default-none"),
            "interface-border-default-primary": obj.get("interface-border-default-primary"),
            "interface-border-disabled-disabled": obj.get("interface-border-disabled-disabled"),
            "interface-border-validation-danger": obj.get("interface-border-validation-danger"),
            "interface-border-validation-success": obj.get("interface-border-validation-success"),
            "interface-border-validation-warning": obj.get("interface-border-validation-warning"),
            "interface-foreground-brand-on-primary": obj.get("interface-foreground-brand-on-primary"),
            "interface-foreground-brand-on-secondary": obj.get("interface-foreground-brand-on-secondary"),
            "interface-foreground-brand-primary": obj.get("interface-foreground-brand-primary"),
            "interface-foreground-brand-secondary": obj.get("interface-foreground-brand-secondary"),
            "interface-foreground-default-inverted": obj.get("interface-foreground-default-inverted"),
            "interface-foreground-default-primary": obj.get("interface-foreground-default-primary"),
            "interface-foreground-default-secondary": obj.get("interface-foreground-default-secondary"),
            "interface-foreground-default-tertiary": obj.get("interface-foreground-default-tertiary"),
            "interface-foreground-disabled-disabled": obj.get("interface-foreground-disabled-disabled"),
            "interface-foreground-disabled-on-disabled": obj.get("interface-foreground-disabled-on-disabled"),
            "interface-foreground-validation-danger": obj.get("interface-foreground-validation-danger"),
            "interface-foreground-validation-success": obj.get("interface-foreground-validation-success"),
            "interface-foreground-validation-warning": obj.get("interface-foreground-validation-warning"),
            "ory-background-default": obj.get("ory-background-default"),
            "ory-border-default": obj.get("ory-border-default"),
            "ory-foreground-default": obj.get("ory-foreground-default"),
            "radio-background-checked": obj.get("radio-background-checked"),
            "radio-background-default": obj.get("radio-background-default"),
            "radio-border-checked": obj.get("radio-border-checked"),
            "radio-border-default": obj.get("radio-border-default"),
            "radio-foreground-checked": obj.get("radio-foreground-checked"),
            "radio-foreground-default": obj.get("radio-foreground-default"),
            "toggle-background-checked": obj.get("toggle-background-checked"),
            "toggle-background-default": obj.get("toggle-background-default"),
            "toggle-border-checked": obj.get("toggle-border-checked"),
            "toggle-border-default": obj.get("toggle-border-default"),
            "toggle-foreground-checked": obj.get("toggle-foreground-checked"),
            "toggle-foreground-default": obj.get("toggle-foreground-default"),
            "ui-100": obj.get("ui-100"),
            "ui-200": obj.get("ui-200"),
            "ui-300": obj.get("ui-300"),
            "ui-400": obj.get("ui-400"),
            "ui-50": obj.get("ui-50"),
            "ui-500": obj.get("ui-500"),
            "ui-600": obj.get("ui-600"),
            "ui-700": obj.get("ui-700"),
            "ui-800": obj.get("ui-800"),
            "ui-900": obj.get("ui-900"),
            "ui-950": obj.get("ui-950"),
            "ui-black": obj.get("ui-black"),
            "ui-danger": obj.get("ui-danger"),
            "ui-success": obj.get("ui-success"),
            "ui-transparent": obj.get("ui-transparent"),
            "ui-warning": obj.get("ui-warning"),
            "ui-white": obj.get("ui-white")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


