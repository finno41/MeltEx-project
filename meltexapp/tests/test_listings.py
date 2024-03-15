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
from meltexapp.helper.geography import get_geography_ids
from meltexapp.helper.asset_class import get_available_ac_ids
from meltexapp.views.views import get_listings, load_listings_table
from meltexapp.config.listing import get_listing_title_map, get_default_listing_columns
from bs4 import BeautifulSoup


class APITests(TestCase):
    @classmethod
    def setUpTestData(self):
        run_seed(None, None)
        self.user = User.objects.get(id=MASTER_USER_ID)
        self.factory = RequestFactory()

    user = User.objects.get(id=MASTER_USER_ID)
    all_columns = get_all_listing_columns()
    default_listing_columns = get_default_listing_columns()
    all_geographies = get_geography_ids(user)
    all_asset_classes = get_available_ac_ids(user)
    url_variables = ["all_listings", "my_listings"]
    params_data = [
        {
            "key": "ac_id",
            "param_values": all_asset_classes,
        },
        {
            "key": "geographies",
            "param_values": all_geographies,
        },
        {
            "key": "columns",
            "param_values": all_columns,
        },
    ]
    test_data = generate_test_cases(user, params_data, url_variables)

    @parameterized.expand(test_data)
    def test_listing_connects(self, i, params, url_variable):
        test_name = f"listing_api_test_{i}"
        request = self.factory.get(f"/listings/{url_variable}", params)
        request.user = self.user
        response = get_listings(request, url_variable)
        print(f"running {test_name} at /listings/{url_variable}")

        self.assertEqual(
            response.status_code,
            200,
            f"Test case '{test_name}' with params: 'f{params}' failed.",
        )

    @parameterized.expand(test_data)
    def test_reload_table_api(self, i, params, url_variable):
        test_name = f"API_table_reload_test_{i}"
        request = self.factory.get(
            f"/listings/load_listings_table/{url_variable}", params
        )
        print(f"running {test_name} at /listings/load_listings_table/{url_variable}")
        request.user = self.user
        response = load_listings_table(request, url_variable)
        with self.subTest(
            test_name=test_name, params=params, url_variable=url_variable
        ):
            self.assertEqual(
                response.status_code,
                200,
                f"Test case '{test_name}' with params: 'f{params}' failed.",
            )
            html_content = response.content.decode("utf-8")
            starting_table_element = "<colgroup>"
            self.assertTrue(html_content.startswith(starting_table_element))

    @parameterized.expand(test_data)
    def test_listing_filters(self, i, params, url_variable):
        test_name = f"listing_filter_test_{i}"
        request = self.factory.get(f"/listings/{url_variable}", params)
        print(f"running {test_name} at /listings/{url_variable}")
        request.user = self.user
        response = get_listings(request, url_variable)
        html_content = response.content.decode("utf-8")
        soup = BeautifulSoup(html_content, "html.parser")
        columns = [
            column.get_text() for column in soup.find_all(class_="listing-column")
        ]
        expected_column_keys = (
            params["columns"]
            if params.get("columns")
            else get_default_listing_columns()
        )
        listing_title_lookup = get_listing_title_map()
        expected_columns = [
            listing_title_lookup[column_key] for column_key in expected_column_keys
        ]
        self.assertListEqual(
            columns, expected_columns, "Columns aren't filtering correctly"
        )
