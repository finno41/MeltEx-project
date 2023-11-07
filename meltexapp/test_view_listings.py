from meltexapp.config.listing import ALL_LISTING_COLUMNS
from meltexapp.global_variables import MASTER_USER_ID
from meltexapp.data.asset_class import get_permitted_asset_classes
from meltexapp.data.sub_asset_class import get_permitted_sub_asset_classes
from meltexapp.data.geography import get_permitted_geographies
from meltexapp.views.views import get_listings
from meltexapp.test.helper import get_list_samples
from django.contrib.auth import get_user_model
from meltexapp.models import User
from django.test import Client, TransactionTestCase


# create a list of all possible circumstances
class ViewListingsTestCase(TransactionTestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "password"
        self.url = "/listings"
        user = User.objects.get(id=MASTER_USER_ID)
        asset_classes = get_permitted_asset_classes(user)
        self.asset_class_ids = [ac.pk for ac in asset_classes]
        self.column_lists = get_list_samples(ALL_LISTING_COLUMNS)
        print("set up complete...")


    def test_response(self):
        print("starting response test")
        print(f"ac_ids:{self.asset_class_ids}")
        responses = get_responses(
            self.asset_class_ids, self.column_lists, self.username, self.password, self.url)
        print(f"responses: {responses}")
        for r in responses:
            print(r.status_code)
            self.assertEqual(r.status_code, 200)


# check that all of these return a page
# check that the data is what we would expect to see

def get_responses(asset_class_ids, column_lists, username, password, base_url):
    responses = []
    for ac_id in asset_class_ids:
        for col_list in column_lists:
            client = Client()
            client.login(username=username, password=password)
            url = "?" + base_url
            for col in col_list:
                url += f"&columns={col}"
            url += f"ac_id={ac_id}"
            responses.append(client.get(url))
    return responses
