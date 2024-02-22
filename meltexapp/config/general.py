PERMISSION_OPTIONS = [
    {"name": "Private", "key": "user"},
    {"name": "Company", "key": "company"},
]

DEFAULT_PERMISSION_KEY = "company"


def permissions_key_value_dict():
    return {option["key"]: option["name"] for option in PERMISSION_OPTIONS}


def permissions_key_value_tuples():
    return [(option["key"], option["name"]) for option in PERMISSION_OPTIONS]
