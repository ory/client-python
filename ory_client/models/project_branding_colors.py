# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.15.4
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

class ProjectBrandingColors(BaseModel):
    """
    ProjectBrandingColors
    """ # noqa: E501
    accent_default_color: Optional[StrictStr] = Field(default=None, description="AccentDefaultColor is a hex color code used by the Ory Account Experience theme.")
    accent_disabled_color: Optional[StrictStr] = Field(default=None, description="AccentDisabledColor is a hex color code used by the Ory Account Experience theme.")
    accent_emphasis_color: Optional[StrictStr] = Field(default=None, description="AccentEmphasisColor is a hex color code used by the Ory Account Experience theme.")
    accent_muted_color: Optional[StrictStr] = Field(default=None, description="AccentMutedColor is a hex color code used by the Ory Account Experience theme.")
    accent_subtle_color: Optional[StrictStr] = Field(default=None, description="AccentSubtleColor is a hex color code used by the Ory Account Experience theme.")
    background_canvas_color: Optional[StrictStr] = Field(default=None, description="BackgroundCanvasColor is a hex color code used by the Ory Account Experience theme.")
    background_subtle_color: Optional[StrictStr] = Field(default=None, description="BackgroundSubtleColor is a hex color code used by the Ory Account Experience theme.")
    background_surface_color: Optional[StrictStr] = Field(default=None, description="BackgroundSurfaceColor is a hex color code used by the Ory Account Experience theme.")
    border_default_color: Optional[StrictStr] = Field(default=None, description="BorderDefaultColor is a hex color code used by the Ory Account Experience theme.")
    error_default_color: Optional[StrictStr] = Field(default=None, description="ErrorDefaultColor is a hex color code used by the Ory Account Experience theme.")
    error_emphasis_color: Optional[StrictStr] = Field(default=None, description="ErrorEmphasisColor is a hex color code used by the Ory Account Experience theme.")
    error_muted_color: Optional[StrictStr] = Field(default=None, description="ErrorMutedColor is a hex color code used by the Ory Account Experience theme.")
    error_subtle_color: Optional[StrictStr] = Field(default=None, description="ErrorSubtleColor is a hex color code used by the Ory Account Experience theme.")
    foreground_default_color: Optional[StrictStr] = Field(default=None, description="ForegroundDefaultColor is a hex color code used by the Ory Account Experience theme.")
    foreground_disabled_color: Optional[StrictStr] = Field(default=None, description="ForegroundDisabledColor is a hex color code used by the Ory Account Experience theme.")
    foreground_muted_color: Optional[StrictStr] = Field(default=None, description="ForegroundMutedColor is a hex color code used by the Ory Account Experience theme.")
    foreground_on_accent_color: Optional[StrictStr] = Field(default=None, description="ForegroundOnAccentColor is a hex color code used by the Ory Account Experience theme.")
    foreground_on_dark_color: Optional[StrictStr] = Field(default=None, description="ForegroundOnDarkColor is a hex color code used by the Ory Account Experience theme.")
    foreground_on_disabled_color: Optional[StrictStr] = Field(default=None, description="ForegroundOnDisabledColor is a hex color code used by the Ory Account Experience theme.")
    foreground_subtle_color: Optional[StrictStr] = Field(default=None, description="ForegroundSubtleColor is a hex color code used by the Ory Account Experience theme.")
    input_background_color: Optional[StrictStr] = Field(default=None, description="InputBackgroundColor is a hex color code used by the Ory Account Experience theme.")
    input_disabled_color: Optional[StrictStr] = Field(default=None, description="InputDisabledColor is a hex color code used by the Ory Account Experience theme.")
    input_placeholder_color: Optional[StrictStr] = Field(default=None, description="InputPlaceholderColor is a hex color code used by the Ory Account Experience theme.")
    input_text_color: Optional[StrictStr] = Field(default=None, description="InputTextColor is a hex color code used by the Ory Account Experience theme.")
    primary_color: Optional[StrictStr] = Field(default=None, description="Primary color is an hsla color value used to derive the other colors from for the Ory Account Experience theme.")
    secondary_color: Optional[StrictStr] = Field(default=None, description="Secondary color is a hsla color code used to derive the other colors from for the Ory Account Experience theme.")
    success_emphasis_color: Optional[StrictStr] = Field(default=None, description="SuccessEmphasisColor is a hex color code used by the Ory Account Experience theme.")
    text_default_color: Optional[StrictStr] = Field(default=None, description="TextDefaultColor is a hex color code used by the Ory Account Experience theme.")
    text_disabled_color: Optional[StrictStr] = Field(default=None, description="TextDisabledColor is a hex color code used by the Ory Account Experience theme.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["accent_default_color", "accent_disabled_color", "accent_emphasis_color", "accent_muted_color", "accent_subtle_color", "background_canvas_color", "background_subtle_color", "background_surface_color", "border_default_color", "error_default_color", "error_emphasis_color", "error_muted_color", "error_subtle_color", "foreground_default_color", "foreground_disabled_color", "foreground_muted_color", "foreground_on_accent_color", "foreground_on_dark_color", "foreground_on_disabled_color", "foreground_subtle_color", "input_background_color", "input_disabled_color", "input_placeholder_color", "input_text_color", "primary_color", "secondary_color", "success_emphasis_color", "text_default_color", "text_disabled_color"]

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
        """Create an instance of ProjectBrandingColors from a JSON string"""
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
        """Create an instance of ProjectBrandingColors from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accent_default_color": obj.get("accent_default_color"),
            "accent_disabled_color": obj.get("accent_disabled_color"),
            "accent_emphasis_color": obj.get("accent_emphasis_color"),
            "accent_muted_color": obj.get("accent_muted_color"),
            "accent_subtle_color": obj.get("accent_subtle_color"),
            "background_canvas_color": obj.get("background_canvas_color"),
            "background_subtle_color": obj.get("background_subtle_color"),
            "background_surface_color": obj.get("background_surface_color"),
            "border_default_color": obj.get("border_default_color"),
            "error_default_color": obj.get("error_default_color"),
            "error_emphasis_color": obj.get("error_emphasis_color"),
            "error_muted_color": obj.get("error_muted_color"),
            "error_subtle_color": obj.get("error_subtle_color"),
            "foreground_default_color": obj.get("foreground_default_color"),
            "foreground_disabled_color": obj.get("foreground_disabled_color"),
            "foreground_muted_color": obj.get("foreground_muted_color"),
            "foreground_on_accent_color": obj.get("foreground_on_accent_color"),
            "foreground_on_dark_color": obj.get("foreground_on_dark_color"),
            "foreground_on_disabled_color": obj.get("foreground_on_disabled_color"),
            "foreground_subtle_color": obj.get("foreground_subtle_color"),
            "input_background_color": obj.get("input_background_color"),
            "input_disabled_color": obj.get("input_disabled_color"),
            "input_placeholder_color": obj.get("input_placeholder_color"),
            "input_text_color": obj.get("input_text_color"),
            "primary_color": obj.get("primary_color"),
            "secondary_color": obj.get("secondary_color"),
            "success_emphasis_color": obj.get("success_emphasis_color"),
            "text_default_color": obj.get("text_default_color"),
            "text_disabled_color": obj.get("text_disabled_color")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


