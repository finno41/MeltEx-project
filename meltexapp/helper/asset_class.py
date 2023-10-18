from meltexapp.data.asset_class import get_permitted_asset_classes


def get_asset_class_options(user):
    acs = get_permitted_asset_classes(user).values("id", "name")
    return acs
