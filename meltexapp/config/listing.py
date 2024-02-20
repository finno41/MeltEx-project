# This also dictates the order of the columns
LISTING_CONFIG = [
    {
        "key": "asset_class_name",
        "name": "Asset Class Name",
        "formatting": None,
        "show": True,
        "default": False,
        "model_key": False,
    },
    {
        "key": "sub_asset_class_name",
        "name": "Sub Asset Class Name",
        "formatting": None,
        "show": True,
        "default": False,
        "model_key": False,
    },
    {
        "key": "geography",
        "name": "Geography",
        "formatting": None,
        "show": True,
        "default": False,
        "model_key": False,
    },
    {
        "key": "impl_approach",
        "name": "Implementation Approach",
        "formatting": None,
        "show": True,
        "default": False,
    },
    {
        "key": "fund_levr",
        "name": "Fund Leverage",
        "formatting": "percentage",
        "show": True,
    },
    {"key": "fund_struc", "name": "Fund Structure", "formatting": None, "show": True},
    {
        "key": "fund_inc_year",
        "name": "Fund Inception Year",
        "formatting": None,
        "show": True,
    },
    {
        "key": "fund_targ_clos_yr",
        "name": "Fund Target Closing Year",
        "formatting": None,
        "show": True,
    },
    {
        "key": "fund_vehi_type",
        "name": "Fund Vehicle Type",
        "formatting": None,
        "show": True,
    },
    {
        "key": "nav",
        "name": "Nav (£m)",
        "formatting": None,
        "show": True,
        "default": True,
    },
    {
        "key": "nav_dis_avl",
        "name": "Nav Discount Available",
        "formatting": "percentage",
        "show": True,
        "default": True,
    },
    {
        "key": "expr_int_ddline",
        "name": "Expression of Interest Deadline",
        "formatting": None,
        "show": True,
        "default": True,
    },
    {
        "key": "targ_irr",
        "name": "Targ IRR p/a",
        "formatting": "percentage",
        "show": True,
        "default": True,
    },
    {"key": "risk_prof", "name": "Risk Profile", "formatting": None, "show": True},
    {"key": "fund_ter", "name": "Fund TER", "formatting": None, "show": True},
    {"key": "comments", "name": "Comments", "formatting": None, "show": True},
    {
        "key": "sub_asset_class",
        "name": "Sub Asset Class",
        "formatting": None,
        "show": False,
    },
]


def get_all_listing_columns():
    return [lc["key"] for lc in LISTING_CONFIG if lc["show"]]


def get_default_listing_columns():
    return [lc["key"] for lc in LISTING_CONFIG if lc.get("default")]


HIDDEN_LISTING_FIELDS = [
    "_state",
    "geography_id",
    "owner_id",
    "public",
    "asset_class_id",
    "sub_asset_class_id",
    "created_on",
    "updated_on",
    "deleted_on",
]


def get_listing_title_map():
    return {lc["key"]: lc["name"] for lc in LISTING_CONFIG}


def get_title_listing_map():
    return {lc["name"]: lc["key"] for lc in LISTING_CONFIG}


def get_listing_k_v_tuple(filter_list=get_default_listing_columns()):
    listing_map = get_listing_title_map()
    return [(col_key, listing_map[col_key]) for col_key in get_all_listing_columns()]


def column_ids_names(filter_list=get_default_listing_columns()):
    listing_map = get_listing_title_map()
    return [
        {"id": col_key, "name": listing_map[col_key]}
        for col_key in get_all_listing_columns()
    ]


def get_column_titles():
    return [lc["name"] for lc in LISTING_CONFIG]


def get_listing_title(listing_key):
    title_map = get_listing_title_map()
    return title_map.get(listing_key, listing_key)


LISTING_REQUIRED_FIELDS = ["geography", "sub_asset_class"]

COLUMN_FORMATTING = {}

SORTABLE_LISTING_HEADERS_LOOKUP = {
    "asset_class_name": "sub_asset_class__asset_class__name",
    "sub_asset_class_name": "sub_asset_class__name",
    "geography": "geography__name",
    "impl_approach": "impl_approach",
    "fund_levr": "fund_levr",
    "fund_struc": "fund_struc",
    "fund_inc_year": "fund_inc_year",
    "fund_targ_clos_yr": "fund_targ_clos_yr",
    "fund_vehi_type": "fund_vehi_type",
    "nav": "nav",
    "nav_dis_avl": "nav_dis_avl",
    "expr_int_ddline": "expr_int_ddline",
    "targ_irr": "targ_irr",
    "risk_prof": "risk_prof",
    "fund_ter": "fund_ter",
}

EDITABLE_LISTING_ATTRS = [
    "geography",
    "sub_asset_class",
    "impl_approach",
    "fund_levr",
    "fund_struc",
    "fund_inc_year",
    "fund_targ_clos_yr",
    "fund_vehi_type",
    "nav",
    "nav_dis_avl",
    "expr_int_ddline",
    "targ_irr",
    "risk_prof",
    "fund_ter",
    "comments",
    "public",
]

FORMATTING_OPTIONS = [{"name": "Percentage", "key": "percentage", "int": 0}]


def get_config_by_key(key):
    return next(lc for lc in LISTING_CONFIG if lc["key"] == key)
