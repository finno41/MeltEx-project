from uuid import UUID


def convert_strings_to_uuids(ids, check=True):
    """
    Checks whether a string is a UUID and converts it if it isn't
    """
    if not check or (ids and isinstance(ids[0], str)):
        return [UUID(id) for id in ids]
    else:
        return ids
