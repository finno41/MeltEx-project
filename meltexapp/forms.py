from django.forms import ModelForm
from django import forms
from meltexapp.models import Listing
from meltexapp.config.listing import get_listing_title
from meltexapp.helper.asset_class import get_asset_class_key_labels
from meltexapp.data.geography import get_permitted_geographies
from meltexapp.models import SubAssetClass


class ListingForm(forms.ModelForm):
    asset_class = forms.ChoiceField()

    class Meta:
        model = Listing
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

    def __init__(self, user, *args, **kwargs):
        AC_CHOICES = (tuple(["", ""]),) + get_asset_class_key_labels(
            user, format="tuple"
        )
        select_fields = ["asset_class", "sub_asset_class", "geography"]
        self.declared_fields["asset_class"].choices = AC_CHOICES
        self.base_fields["expr_int_ddline"] = forms.DateField(
            widget=forms.DateInput(attrs={"type": "date"})
        )
        for field_type, fields in {
            "base_fields": self.base_fields,
            "declared_fields": self.declared_fields,
        }.items():
            for field in fields:
                if field in select_fields:
                    getattr(self, field_type)[field].widget.attrs[
                        "class"
                    ] = "form-select"
                else:
                    getattr(self, field_type)[field].widget.attrs[
                        "class"
                    ] = "form-control"
                if getattr(self, field_type)[field].required:
                    getattr(self, field_type)[field].required = False
                    getattr(self, field_type)[field].widget.attrs["required"] = True

        self.base_fields["sub_asset_class"].queryset = SubAssetClass.objects.none()
        self.base_fields["geography"].queryset = get_permitted_geographies(
            user
        ).order_by("name")
        super(ListingForm, self).__init__(*args, **kwargs)

    field_order = [
        "asset_class",
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
