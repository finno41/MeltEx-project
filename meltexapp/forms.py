from django.forms import ModelForm
from django import forms
from meltexapp.models import Listing
from meltexapp.config.listing import get_listing_title
from meltexapp.helper.asset_class import get_asset_class_key_labels
from meltexapp.models import SubAssetClass


class ListingForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        AC_CHOICES = (tuple(["", ""]),) + get_asset_class_key_labels(
            user, format="tuple"
        )
        super(ListingForm, self).__init__(*args, **kwargs)
        fields = [
            "sub_asset_class",
            "geography",
            "impl_approach",
            "fund_levr",
            "fund_struc",
            "fund_inc_year",
            "fund_targ_clos_yr",
            "fund_vehi_type",
            "nav",
            "nav_dis_avl",
            "targ_irr",
            "risk_prof",
            "fund_ter",
            "comments",
        ]
        select_fields = ["asset_class", "sub_asset_class"]
        start_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
        self.fields["asset_class"] = forms.ChoiceField(choices=AC_CHOICES)
        self.fields["expr_int_ddline"] = forms.DateField(
            widget=forms.DateInput(attrs={"type": "date"})
        )
        for field in fields:
            self.fields[field] = Listing._meta.get_field(field).formfield()
            self.fields[field].label = get_listing_title(field)
        for field in self.fields:
            if field in select_fields:
                self.fields[field].widget.attrs["class"] = "form-select"
            else:
                self.fields[field].widget.attrs["class"] = "form-control"
            if self.fields[field].required:
                self.fields[field].required = False
                self.fields[field].widget.attrs["required"] = True

        self.fields["sub_asset_class"].queryset = SubAssetClass.objects.none()
