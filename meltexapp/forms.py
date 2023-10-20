from django.forms import ModelForm
from meltexapp.models import Listing
from meltexapp.config.listing import get_listing_title


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
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
        ]

    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = get_listing_title(field)
