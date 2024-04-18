from meltexapp.data.geography import (
    get_permitted_geographies,
    get_geographies_by_ids,
    get_geographies_by_parents,
    get_geographies_by_type,
)
from meltexapp.helper.general import convert_strings_to_uuids
import pandas as pd
from uuid import UUID
import random

def get_available_geographies(user):
    all_geographies = get_permitted_geographies(user)
    return list(all_geographies.values())

def get_geography_ids(user):
    all_geographies = get_available_geographies(user)
    return [geography["id"] for geography in all_geographies]


def get_geography_names(user):
    geographies = get_permitted_geographies(user)
    return list(geographies.values_list("name", flat=True))


def get_all_geography_children(user, ids):
    current_geographies = get_geographies_by_ids(user, ids)
    all_geographies = current_geographies
    while current_geographies:
        current_geographies = get_geographies_by_parents(user, current_geographies)
        all_geographies |= current_geographies
    return all_geographies


def get_random_geography(user, geography_type):
    geographies = get_geographies_by_type(user, type=geography_type)
    count = geographies.count()
    if count < 0:
        raise Exception(
            f"No geography was found for user '{user}' with the geography type {geography_type}"
        )
    index = random.randint(0, count - 1)
    return geographies[index]
