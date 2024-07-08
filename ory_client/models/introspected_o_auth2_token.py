# coding: utf-8

"""
    Ory APIs

    Documentation for all public and administrative Ory APIs. Administrative APIs can only be accessed with a valid Personal Access Token. Public APIs are mostly used in browsers. 

    The version of the OpenAPI document: v1.13.7
    Contact: support@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IntrospectedOAuth2Token(BaseModel):
    """
    Introspection contains an access token's session data as specified by [IETF RFC 7662](https://tools.ietf.org/html/rfc7662)
    """ # noqa: E501
    active: StrictBool = Field(description="Active is a boolean indicator of whether or not the presented token is currently active.  The specifics of a token's \"active\" state will vary depending on the implementation of the authorization server and the information it keeps about its tokens, but a \"true\" value return for the \"active\" property will generally indicate that a given token has been issued by this authorization server, has not been revoked by the resource owner, and is within its given time window of validity (e.g., after its issuance time and before its expiration time).")
    aud: Optional[List[StrictStr]] = Field(default=None, description="Audience contains a list of the token's intended audiences.")
    client_id: Optional[StrictStr] = Field(default=None, description="ID is aclient identifier for the OAuth 2.0 client that requested this token.")
    exp: Optional[StrictInt] = Field(default=None, description="Expires at is an integer timestamp, measured in the number of seconds since January 1 1970 UTC, indicating when this token will expire.")
    ext: Optional[Dict[str, Any]] = Field(default=None, description="Extra is arbitrary data set by the session.")
    iat: Optional[StrictInt] = Field(default=None, description="Issued at is an integer timestamp, measured in the number of seconds since January 1 1970 UTC, indicating when this token was originally issued.")
    iss: Optional[StrictStr] = Field(default=None, description="IssuerURL is a string representing the issuer of this token")
    nbf: Optional[StrictInt] = Field(default=None, description="NotBefore is an integer timestamp, measured in the number of seconds since January 1 1970 UTC, indicating when this token is not to be used before.")
    obfuscated_subject: Optional[StrictStr] = Field(default=None, description="ObfuscatedSubject is set when the subject identifier algorithm was set to \"pairwise\" during authorization. It is the `sub` value of the ID Token that was issued.")
    scope: Optional[StrictStr] = Field(default=None, description="Scope is a JSON string containing a space-separated list of scopes associated with this token.")
    sub: Optional[StrictStr] = Field(default=None, description="Subject of the token, as defined in JWT [RFC7519]. Usually a machine-readable identifier of the resource owner who authorized this token.")
    token_type: Optional[StrictStr] = Field(default=None, description="TokenType is the introspected token's type, typically `Bearer`.")
    token_use: Optional[StrictStr] = Field(default=None, description="TokenUse is the introspected token's use, for example `access_token` or `refresh_token`.")
    username: Optional[StrictStr] = Field(default=None, description="Username is a human-readable identifier for the resource owner who authorized this token.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["active", "aud", "client_id", "exp", "ext", "iat", "iss", "nbf", "obfuscated_subject", "scope", "sub", "token_type", "token_use", "username"]

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
        """Create an instance of IntrospectedOAuth2Token from a JSON string"""
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
        """Create an instance of IntrospectedOAuth2Token from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": obj.get("active"),
            "aud": obj.get("aud"),
            "client_id": obj.get("client_id"),
            "exp": obj.get("exp"),
            "ext": obj.get("ext"),
            "iat": obj.get("iat"),
            "iss": obj.get("iss"),
            "nbf": obj.get("nbf"),
            "obfuscated_subject": obj.get("obfuscated_subject"),
            "scope": obj.get("scope"),
            "sub": obj.get("sub"),
            "token_type": obj.get("token_type"),
            "token_use": obj.get("token_use"),
            "username": obj.get("username")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


