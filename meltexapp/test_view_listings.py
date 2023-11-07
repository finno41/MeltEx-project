from meltexapp.config.listing import ALL_LISTING_COLUMNS
from meltexapp.global_variables import MASTER_USER_ID
from meltexapp.data.asset_class import get_permitted_asset_classes
from meltexapp.data.sub_asset_class import get_permitted_sub_asset_classes
from meltexapp.data.geography import get_permitted_geographies
from meltexapp.views.views import get_listings
from meltexapp.test.helper import get_list_samples
from django.contrib.auth import get_user_model
from meltexapp.management.commands.seed import create_asset_classes, create_company, create_geographies, create_listing
from meltexapp.models import User
from django.test import Client, TransactionTestCase


# create a list of all possible circumstances
class ViewListingsTestCase(TransactionTestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "password"
        self.url = "/listings"
        user = User.objects.create_user(username=self.username, email='test@test.com', password=self.password)
        create_asset_classes(user)
        create_company(user)
        create_geographies(user)
        for i in range(15):
            create_listing(i, user)
        asset_classes = get_permitted_asset_classes(user)
        self.asset_class_ids = [ac.pk for ac in asset_classes]
        self.column_lists = get_list_samples(ALL_LISTING_COLUMNS)
        self.responses = get_responses(
            self.asset_class_ids, self.column_lists, self.username, self.password, self.url)
        print("set up complete...")



    def test_response(self):
        print("starting response test")
        for r in self.responses:
            self.assertEqual(r.status_code, 200)


# check that all of these return a page
# check that the data is what we would expect to see

def get_responses(asset_class_ids, column_lists, username, password, base_url):
    responses = []
    for ac_id in asset_class_ids:
        print(f"testing for asset class {ac_id.hex}")
        for col_list in column_lists:
            client = Client()
            client.login(username=username, password=password)
            url = base_url + "?"
            url += f"ac_id={ac_id}"
            for col in col_list:
                url += f"&columns={col}"
            # /listings?ac_id=fe25d751-c75c-4468-ac0f-dc4cecfbde1d&columns=asset_class_name&columns=sub_asset_class_name
            responses.append(client.get(url))
    return responses
