import random

def get_random_instance(object):
    sub_asset_classes = list(object.objects.all())
    sub_asset_class = random.sample(sub_asset_classes, k=1)
    return sub_asset_class[0]
