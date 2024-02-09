INTEREST_STATUS = [
    {"key": "accepted", "name": "Accepted"},
    {"key": "pending", "name": "Pending"},
    {"key": "rejected", "name": "Rejected"},
]

DEFAULT_INTEREST_STATUS_KEY = "pending"


def interest_status_options_tuple():
    return [(status["key"], status["name"]) for status in INTEREST_STATUS]
