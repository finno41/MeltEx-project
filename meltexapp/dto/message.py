from meltexapp.helper.base_dto import BaseDTOCollection, BaseDTO
from meltexapp.data.message import get_messages_by_register_interest
from meltexapp.data.user import get_users_by_ids
import pandas as pd


class MessageDTO(BaseDTO):
    def __init__(self, message, user, **kwargs):
        if not isinstance(message, dict):
            data = message.__dict__
        self.company_message = message.user.company == user.company

        super().__init__(data, user, **kwargs)


class MessageDTOCollection(BaseDTOCollection):
    def __init__(self, register_interest: object, user):
        messages = get_messages_by_register_interest(user, register_interest)
        super().__init__(
            messages,
            user,
            base_dto=MessageDTO,
        )
