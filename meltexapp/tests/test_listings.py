from django.test import TestCase, RequestFactory
from meltexapp.tests.helper import generate_test_cases
from meltexapp.config.listing import (
    get_all_listing_columns,
    get_default_listing_columns,
)
from meltexapp.management.commands.seed import run_seed
from meltexapp.models import User
from parameterized import parameterized
from meltexapp.global_variables import MASTER_USER_ID
from meltexapp.helper.geography import get_continent_ids
from meltexapp.helper.asset_class import get_available_ac_ids
from meltexapp.views.views import get_listings


class APITests(TestCase):
    @classmethod
    def setUpTestData(self):
        run_seed(None, None)
        self.user = User.objects.get(id=MASTER_USER_ID)
        self.factory = RequestFactory()

    user = User.objects.get(id=MASTER_USER_ID)
    all_columns = get_all_listing_columns()
    default_listing_columns = get_default_listing_columns()
    all_continents = get_continent_ids(user)
    all_asset_classes = get_available_ac_ids(user)
    url_variables = ["all_listings", "my_listings"]
    params_data = [
        {
            "key": "ac_id",
            "param_values": all_asset_classes,
        },
        {
            "key": "continents",
            "param_values": all_continents,
        },
        {
            "key": "columns",
            "param_values": all_columns,
        },
    ]
    test_data = generate_test_cases(user, params_data, url_variables)

    @parameterized.expand(test_data)
    def test_listing_connects(self, name, params, url_variable):
        request = self.factory.get(f"/listings/{url_variable}", params)
        request.user = self.user
        response = get_listings(request, url_variable)
        print(f"running test {name} at /listings/{url_variable}")

        self.assertEqual(
            response.status_code,
            200,
            f"Test case '{name}' with params: 'f{params}' failed.",
        )
