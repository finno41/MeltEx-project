PERMISSION_OPTIONS = [
    {"name": "Private", "key": "user"},
    {"name": "Company", "key": "company"},
]

DEFAULT_PERMISSION_KEY = "company"


def permissions_key_value_dict():
    return {option["key"]: option["name"] for option in PERMISSION_OPTIONS}


def permissions_key_value_tuples():
    return [(option["key"], option["name"]) for option in PERMISSION_OPTIONS]


def get_config_by_key(key, config):
    return next(lc for lc in config if lc["key"] == key)
