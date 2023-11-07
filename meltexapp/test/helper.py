import random

def get_list_samples(list):
    length = len(list)
    sampled_list = [random.sample(list, i) for i in range(length + 1)]
    return sampled_list
