import random
from itertools import combinations
from meltexapp.models import User
from meltexapp.config.listing import (
    get_all_listing_columns,
    get_default_listing_columns,
)
from meltexapp.models import User
from meltexapp.global_variables import MASTER_USER_ID
from meltexapp.helper.geography import get_continent_ids
from meltexapp.helper.asset_class import get_available_ac_ids


def get_list_samples(list):
    length = len(list)
    sampled_list = [random.sample(list, i) for i in range(length + 1)]
    return sampled_list


def get_all_combinations(lst: list) -> list:
    all_combinations = []
    for r in range(len(lst) + 1):
        for subset in combinations(lst, r):
            all_combinations.append(list(subset))
    return all_combinations


def get_sample_of_combinations(lst: list) -> list:
    list_len = len(lst)
    singular_list = [[l] for l in lst]
    sample_list = [random.sample(lst, i) for i in range(list_len)]
    return singular_list + sample_list


def generate_test_cases(user, params_data: list, url_variables: list):
    param_settings = [
        {
            "param_name": param["key"],
            "params": get_sample_of_combinations(param["param_values"]),
        }
        for param in params_data
    ]
    param_settings = sorted(
        param_settings, key=lambda x: len(x["params"]), reverse=True
    )
    longest_params_len = len(param_settings[0]["params"])
    return [
        (
            i + 1,
            {
                param_setting["param_name"]: param_setting["params"][
                    i % len(param_setting["params"])
                ]
                for param_setting in param_settings
            },
            url_variables[i % len(url_variables)],
        )
        for i in range(longest_params_len)
    ]
