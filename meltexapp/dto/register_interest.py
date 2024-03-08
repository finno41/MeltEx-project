from meltexapp.helper.base_dto import BaseDTOCollection, BaseDTO
from meltexapp.data.user import get_users_by_ids
from meltexapp.config.register_interest import (
    HIDDEN_REG_INTEREST_FIELDS,
)
from meltexapp.config.geography import COUNTRY_CODE_LOOKUP
import pandas as pd


class RegisterInterestDTO(BaseDTO):
    def __init__(
        self, data, user, user_type, hide_keys=HIDDEN_REG_INTEREST_FIELDS, **kwargs
    ):
        if not isinstance(data, dict):
            data = data.__dict__

        super().__init__(data, user, hide_keys=hide_keys, **kwargs)


class RegisterInterestDTOCollection(BaseDTOCollection):
    def __init__(self, data, user, user_type, hide_keys=HIDDEN_REG_INTEREST_FIELDS):
        if not isinstance(data, list):
            data = list(data.values())
        user_ids = [d["buyer_user_id"] for d in data]
        user_queryset = get_users_by_ids(user_ids)
        user_display_attrs = [
            "first_name",
            "last_name",
            "company__name",
            "job_title",
        ]
        self.link_model(
            "user", user, "buyer_user_id", "id", user_queryset, user_display_attrs
        )
        super().__init__(
            data,
            user,
            base_dto=RegisterInterestDTO,
            user_type=user_type,
            hide_keys=hide_keys,
        )
