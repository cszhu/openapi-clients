# coding: utf-8

"""
    Visier Consolidated Analytics APIs

    Visier APIs for managing consolidated analytics (CA) tenants.

    The version of the OpenAPI document: 22222222.99201.1401
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from visier.api.consolidated_analytics.models.consolidated_analytics_api_tenant_with_details import ConsolidatedAnalyticsAPITenantWithDetails
from typing import Optional, Set
from typing_extensions import Self

class ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO(BaseModel):
    """
    ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO
    """ # noqa: E501
    tenants: Optional[List[ConsolidatedAnalyticsAPITenantWithDetails]] = Field(default=None, description="A list of CA tenants and their details.")
    __properties: ClassVar[List[str]] = ["tenants"]

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
        """Create an instance of ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tenants (list)
        _items = []
        if self.tenants:
            for _item in self.tenants:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tenants'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConsolidatedAnalyticsAPITenantWithDetailsListResponseDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenants": [ConsolidatedAnalyticsAPITenantWithDetails.from_dict(_item) for _item in obj["tenants"]] if obj.get("tenants") is not None else None
        })
        return _obj


