from django.test import TestCase, RequestFactory
from meltexapp.tests.helper import get_sample_of_combinations
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

    def generate_test_cases():
        user = User.objects.get(id=MASTER_USER_ID)
        all_columns = get_all_listing_columns()
        default_listing_columns = get_default_listing_columns()
        column_selections = get_sample_of_combinations(all_columns)
        all_continents = get_continent_ids(user)
        continents_selection = get_sample_of_combinations(all_continents)
        all_asset_classes = get_available_ac_ids(user)
        asset_class_selection = get_sample_of_combinations(all_asset_classes)
        param_settings = [
            {
                "param_name": "ac_id",
                "params": asset_class_selection,
            },
            {
                "param_name": "continents",
                "params": continents_selection,
            },
            {
                "param_name": "columns",
                "params": column_selections,
            },
        ]
        param_settings = sorted(
            param_settings, key=lambda x: len(x["params"]), reverse=True
        )
        return [
            (
                f"listing_API_test_{i}",
                {
                    param_setting["param_name"]: param_setting["params"][
                        i % len(param_setting["params"])
                    ]
                    for param_setting in param_settings
                },
            )
            for i in range(len(param_settings[0]["params"]))
        ]

    @parameterized.expand(generate_test_cases)
    def test_listing_connects(self, name, params):
        request = self.factory.get("/listings", params)
        request.user = self.user
        response = get_listings(request)
        print(f"running test {name}")
        print(response)

        self.assertEqual(
            response.status_code,
            200,
            f"Test case '{name}' with params: 'f{params}' failed.",
        )
