from django.test import TestCase, RequestFactory
from meltexapp.tests.helper import get_all_combinations
from meltexapp.config.listing import (
    get_all_listing_columns,
    get_default_listing_columns,
)
from meltexapp.management.commands.seed import run_seed
from meltexapp.models import User
from parameterized import parameterized
from meltexapp.global_variables import MASTER_USER_ID
from meltexapp.helper.geography import get_continents_countries
from meltexapp.helper.asset_class import get_available_ac_ids
from meltexapp.views.views import get_listings


class APITests(TestCase):
    def setUp(self):
        run_seed(None, None)
        self.user = User.objects.get(id=MASTER_USER_ID)
        self.factory = RequestFactory()
        self.all_columns = get_all_listing_columns()
        self.default_listing_columns = get_default_listing_columns()
        self.column_selections = get_all_combinations(self.all_columns)
        self.all_continents = get_continents_countries(self.user, continents_only=True)
        self.continents_selection = get_all_combinations(self.all_continents)
        self.all_asset_classes = get_available_ac_ids(self.user)
        self.asset_class_selection = get_all_combinations(self.all_asset_classes)
        self.param_settings = [
            {
                "param_name": "ac_id",
                "params": self.asset_class_selection,
            },
            {
                "param_name": "continents",
                "params": self.continents_selection,
            },
            {
                "param_name": "columns",
                "params": self.column_selections,
            },
        ]
        self.param_settings = sorted(
            self.param_settings, key=lambda x: len(x["params"]), reverse=True
        )

    def generate_test_cases(self):
        return [
            (
                f"listing_API_test_{i}",
                {
                    param_setting["param_name"]: param_setting["params"][
                        i % len(param_setting["params"])
                    ]
                    for param_setting in self.param_settings
                },
            )
            for i in range(len(self.param_settings[0]["params"]))
        ]

    # test_case_int, int should increase by 1 each time
    # identify which param is the longest in length and loop through it
    # use modulo on the length of the remaining params to grab the params
    @parameterized.expand(generate_test_cases)
    def test_listing_connects(self, name, params):
        request = self.factory.get("/listings")
        request.user = self.user
        response = get_listings(request)

        self.assertEqual(
            response.status_code,
            200,
            f"Test case '{name}' with params: 'f{params}' failed.",
        )
