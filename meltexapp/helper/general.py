from uuid import UUID
import pandas as pd


def convert_strings_to_uuids(ids, check=True):
    """
    Checks whether a string is a UUID and converts it if it isn't
    """
    if not check or (ids and isinstance(ids[0], str)):
        return [UUID(id) for id in ids]
    else:
        return ids


def bulk_manipulate_dict_list(list_of_dicts, from_to_map: dict = {}, add_keys={}):
    """
    Uses Pandas to manipulate lists of dicts.
    Mass change keys using from_to_map to change key names, add keys with the same value using add_keys
    """
    df = pd.DataFrame(list_of_dicts)
    if from_to_map:
        df = df.rename(columns=from_to_map)
    for key, value in add_keys.items():
        df[key] = value
    return df.to_dict("records")
