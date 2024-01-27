from meltexapp.data.asset_class import get_permitted_asset_classes


def get_asset_class_options(user):
    acs = list(get_permitted_asset_classes(user).values("id", "name"))
    acs = [{"id": ac["id"].hex, "name": ac["name"]} for ac in acs]
    return acs


def get_asset_class_key_labels(user, format):
    acs = get_permitted_asset_classes(user)
    acs = acs.values("id", "name")
    if format == "tuple":
        return tuple((ac["id"], ac["name"]) for ac in acs)


def get_asset_class_names(user):
    acs = get_permitted_asset_classes(user)
    return list(acs.values_list("name", flat=True))


def get_asset_class_from_listing(listing):
    return listing.sub_asset_class.asset_class


def get_available_ac_ids(user):
    acs = get_permitted_asset_classes(user)
    ac_ids = acs.values_list("id", flat=True)
    return [ac_id.hex for ac_id in ac_ids]
