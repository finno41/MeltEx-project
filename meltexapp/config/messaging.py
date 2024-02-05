MESSAGE_STATUSES = [
    {"key": "accepted", "name": "Accepted"},
    {"key": "pending", "name": "Pending"},
    {"key": "rejected", "name": "Rejected"},
]

DEFAULT_MESSAGE_KEY = "pending"


def message_options_tuple():
    return [(status["key"], status["name"]) for status in MESSAGE_STATUSES]
