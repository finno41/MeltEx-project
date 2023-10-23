from django.forms import ModelForm
from django import forms
from meltexapp.models import Listing
from meltexapp.config.listing import get_listing_title
from meltexapp.helper.asset_class import get_asset_class_key_labels
from meltexapp.models import SubAssetClass


class ListingForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        AC_CHOICES = get_asset_class_key_labels(user, format="tuple")
        super(ListingForm, self).__init__(*args, **kwargs)
        fields = [
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
        self.fields["asset_class"] = forms.ChoiceField(choices=AC_CHOICES)
        for field in fields:
            self.fields[field] = Listing._meta.get_field(field).formfield()
            self.fields[field].label = get_listing_title(field)
        self.fields["sub_asset_class"].queryset = SubAssetClass.objects.none()
