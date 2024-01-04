from meltexapp.config.listing import get_all_listing_columns
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
        print("creating setup...")
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
        self.column_lists = get_list_samples(get_all_listing_columns())
        print("setup complete.")
        print("testing responses...")
        self.responses = self.test_get_responses()


    def test_get_responses(self):
        print("starting response test")
        responses = []
        for ac_id in self.asset_class_ids:
            print(f"testing for asset class {ac_id.hex}")
            for col_list in self.column_lists:
                client = Client()
                client.login(username=self.username, password=self.password)
                url = self.url + "?"
                url += f"ac_id={ac_id}"
                for col in col_list:
                    url += f"&columns={col}"
                try:
                    responses.append({"response": client.get(url), "url": url})
                except Exception as e:
                    self.fail(msg=f"url: {url}\nfailed with error message:\n {str(e)}")
        return responses


    def test_response_status(self):
        print("starting response test")
        for r in self.responses:
            response = r["response"]
            url = r["url"]
            self.assertEqual(response.status_code, 200)



# check that all of these return a page
# check that the data is what we would expect to see
