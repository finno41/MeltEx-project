from meltexapp.data.asset_class import get_permitted_asset_classes


def get_asset_class_options(user):
    acs = get_permitted_asset_classes(user).values("id", "name")
    return acs


def get_asset_class_key_labels(user, format):
    acs = get_permitted_asset_classes(user)
    acs = acs.values("id", "name")
    if format == "tuple":
        return tuple((ac["id"], ac["name"]) for ac in acs)
