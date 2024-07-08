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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from ory_client.models.plan_details import PlanDetails
from typing import Optional, Set
from typing_extensions import Self

class Subscription(BaseModel):
    """
    Subscription
    """ # noqa: E501
    created_at: datetime
    currency: StrictStr = Field(description="The currency of the subscription. To change this, a new subscription must be created. usd USD eur Euro")
    current_interval: StrictStr = Field(description="The currently active interval of the subscription monthly Monthly yearly Yearly")
    current_plan: StrictStr = Field(description="The currently active plan of the subscription")
    current_plan_details: Optional[PlanDetails] = None
    customer_id: StrictStr = Field(description="The ID of the stripe customer")
    id: StrictStr = Field(description="The ID of the subscription")
    interval_changes_to: Optional[StrictStr]
    ongoing_stripe_checkout_id: Optional[StrictStr] = None
    payed_until: datetime = Field(description="Until when the subscription is payed")
    plan_changes_at: Optional[datetime] = None
    plan_changes_to: Optional[StrictStr]
    status: StrictStr = Field(description="For `collection_method=charge_automatically` a subscription moves into `incomplete` if the initial payment attempt fails. A subscription in this status can only have metadata and default_source updated. Once the first invoice is paid, the subscription moves into an `active` status. If the first invoice is not paid within 23 hours, the subscription transitions to `incomplete_expired`. This is a terminal status, the open invoice will be voided and no further invoices will be generated.  A subscription that is currently in a trial period is `trialing` and moves to `active` when the trial period is over.  A subscription can only enter a `paused` status [when a trial ends without a payment method](https://stripe.com/billing/subscriptions/trials#create-free-trials-without-payment). A `paused` subscription doesn't generate invoices and can be resumed after your customer adds their payment method. The `paused` status is different from [pausing collection](https://stripe.com/billing/subscriptions/pause-payment), which still generates invoices and leaves the subscription's status unchanged.  If subscription `collection_method=charge_automatically`, it becomes `past_due` when payment is required but cannot be paid (due to failed payment or awaiting additional user actions). Once Stripe has exhausted all payment retry attempts, the subscription will become `canceled` or `unpaid` (depending on your subscriptions settings).  If subscription `collection_method=send_invoice` it becomes `past_due` when its invoice is not paid by the due date, and `canceled` or `unpaid` if it is still not paid by an additional deadline after that. Note that when a subscription has a status of `unpaid`, no subsequent invoices will be attempted (invoices will be created, but then immediately automatically closed). After receiving updated payment information from a customer, you may choose to reopen and pay their closed invoices.")
    stripe_checkout_expires_at: Optional[datetime] = None
    updated_at: datetime
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["created_at", "currency", "current_interval", "current_plan", "current_plan_details", "customer_id", "id", "interval_changes_to", "ongoing_stripe_checkout_id", "payed_until", "plan_changes_at", "plan_changes_to", "status", "stripe_checkout_expires_at", "updated_at"]

    @field_validator('currency')
    def currency_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['usd', 'eur']):
            raise ValueError("must be one of enum values ('usd', 'eur')")
        return value

    @field_validator('current_interval')
    def current_interval_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['monthly', 'yearly']):
            raise ValueError("must be one of enum values ('monthly', 'yearly')")
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
        """Create an instance of Subscription from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "currency",
            "current_interval",
            "current_plan",
            "customer_id",
            "id",
            "payed_until",
            "updated_at",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of current_plan_details
        if self.current_plan_details:
            _dict['current_plan_details'] = self.current_plan_details.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if interval_changes_to (nullable) is None
        # and model_fields_set contains the field
        if self.interval_changes_to is None and "interval_changes_to" in self.model_fields_set:
            _dict['interval_changes_to'] = None

        # set to None if ongoing_stripe_checkout_id (nullable) is None
        # and model_fields_set contains the field
        if self.ongoing_stripe_checkout_id is None and "ongoing_stripe_checkout_id" in self.model_fields_set:
            _dict['ongoing_stripe_checkout_id'] = None

        # set to None if plan_changes_to (nullable) is None
        # and model_fields_set contains the field
        if self.plan_changes_to is None and "plan_changes_to" in self.model_fields_set:
            _dict['plan_changes_to'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Subscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "currency": obj.get("currency"),
            "current_interval": obj.get("current_interval"),
            "current_plan": obj.get("current_plan"),
            "current_plan_details": PlanDetails.from_dict(obj["current_plan_details"]) if obj.get("current_plan_details") is not None else None,
            "customer_id": obj.get("customer_id"),
            "id": obj.get("id"),
            "interval_changes_to": obj.get("interval_changes_to"),
            "ongoing_stripe_checkout_id": obj.get("ongoing_stripe_checkout_id"),
            "payed_until": obj.get("payed_until"),
            "plan_changes_at": obj.get("plan_changes_at"),
            "plan_changes_to": obj.get("plan_changes_to"),
            "status": obj.get("status"),
            "stripe_checkout_expires_at": obj.get("stripe_checkout_expires_at"),
            "updated_at": obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


