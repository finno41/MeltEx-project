from meltexapp.data.sub_asset_class import get_permitted_sub_asset_classes


def get_sub_asset_class_names(user):
    sub_acs = get_permitted_sub_asset_classes(user)
    return list(sub_acs.values_list("name", flat=True))
