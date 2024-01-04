import random
from itertools import combinations


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
    singular_list = [l for l in lst]
    sample_list = [random.sample(lst, i) for i in range(list_len)]
    return singular_list + sample_list
