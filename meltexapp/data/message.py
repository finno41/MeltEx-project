from meltexapp.models import Message
from meltexapp.helper.register_interest import is_user_permitted_reg_interest


def get_messages_by_register_interest(user, register_interest):
    if not is_user_permitted_reg_interest(user, register_interest):
        raise Exception("You are not authorised to view these messages")
    return Message.objects.filter(register_interest=register_interest)
