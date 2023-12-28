from django.core.management.base import BaseCommand
from meltexapp.models import (
    AssetClass,
    SubAssetClass,
    Geography,
    Listing,
    Company,
    User,
)
from meltexapp.helper.model import get_random_instance
import pandas as pd
import random


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self, options["mode"])
        self.stdout.write("done.")


def clear_data():
    """Deletes all the table data"""
    print("Delete Asset Class instances")
    AssetClass.objects.all().delete()
    print("Delete Geography instances")
    Geography.objects.all().delete()
    print("Delete Listing instances")
    Listing.objects.all().delete()


def create_company(user=False):
    """Creates an address object combining different elements from the list"""
    if not user:
        user = User.objects.get(username="admin_oli")
        stu_user = User.objects.get(username="admin_stu")
    try:
        company = Company.objects.get(name="MeltEx")
        print("company MeltEx exists")
    except:
        print("creating MeltEx")
        company = Company()
        company.name = "MeltEx"
        company.type = "Admin"
        company.save()
        user.company = company
        stu_user.company = company
        user.save()
        stu_user.save()
    return company


def create_geographies(user=False):
    if not user:
        user = User.objects.get(username="admin_oli")
    country_df = pd.read_excel(
        "meltexapp/seeding/seed_data/seed_data.xlsx", sheet_name="Geography Data"
    )
    continents = list(set(country_df["Continent"]))
    for continent in continents:
        print(f"creating {continent}")
        geography = Geography()
        geography.name = continent
        geography.owner = user
        geography.save()
    geo_mapper = list(
        Geography.objects.filter(parent_id__isnull=True).values("name", "id")
    )
    geo_mapper = {gm["name"]: gm["id"].hex for gm in geo_mapper}
    for i, row in country_df.iterrows():
        print(f"creating {row['Country']}")
        geography = Geography()
        geography.name = row["Country"]
        geography.parent_id = geo_mapper[row["Continent"]]
        geography.owner = user
        geography.save()


def create_asset_classes(user=False):
    if not user:
        user = User.objects.get(username="admin_oli")
    ac_df = pd.read_excel(
        "meltexapp/seeding/seed_data/seed_data.xlsx", sheet_name="Asset Class Data"
    )
    asset_classes = list(set(ac_df["Asset Class"]))
    for ac in asset_classes:
        print(f"creating {ac}")
        asset_class = AssetClass()
        asset_class.name = ac
        asset_class.owner = user
        asset_class.save()
    ac_mapper = {ac.name: ac for ac in list(AssetClass.objects.all())}
    for i, row in ac_df.iterrows():
        print(f"creating {row['Sub Asset Class']}")
        sub_ac = SubAssetClass()
        sub_ac.name = row["Sub Asset Class"]
        sub_ac.asset_class = ac_mapper[row["Asset Class"]]
        sub_ac.owner = user
        sub_ac.save()


def create_listing(i, user=False):
    print(f"creating listing {i+1}")
    if not user:
        user = User.objects.get(username="admin_oli")
    sub_asset_class = get_random_instance(SubAssetClass)
    asset_class = sub_asset_class.asset_class
    geography = get_random_instance(Geography)
    listing = Listing()
    listing.sub_asset_class = sub_asset_class
    listing.geography = geography
    listing.impl_approach = "Test"
    listing.fund_levr = round(random.uniform(0.00, 30.00), 2)
    listing.fund_struc = "test fund struc"
    listing.fund_inc_year = 2020
    listing.fund_targ_clos_yr = 2023
    listing.fund_vehi_type = "test fund vehi type"
    listing.nav = round(random.uniform(0.00, 30.00), 2)
    listing.nav_dis_avl = round(random.uniform(0.00, 30.00), 2)
    listing.expr_int_ddline = "2024-02-02"
    listing.targ_irr = round(random.uniform(0.00, 30.00), 2)
    listing.risk_prof = "test risk prof"
    listing.fund_ter = round(random.uniform(0.00, 30.00), 2)
    listing.owner = user
    listing.comments = "This is a test comment"
    listing.save()
    return listing


def run_seed(self, mode):
    """Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    create_company()
    create_geographies()
    create_asset_classes()

    # Creating listings
    for i in range(200):
        create_listing(i)
