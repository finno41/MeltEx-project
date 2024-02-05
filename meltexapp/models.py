from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from meltexapp.config.general import (
    permissions_key_value_tuples,
    DEFAULT_PERMISSION_KEY,
)
from meltexapp.config.messaging import message_options_tuple, DEFAULT_MESSAGE_KEY


class BaseModel(models.model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(blank=True, null=True)


class Company(BaseModel):
    name = models.CharField(max_length=50, blank=False, null=False)
    type = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, blank=True, null=True
    )
    subscriber = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class AssetClass(BaseModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name


class SubAssetClass(BaseModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    asset_class = models.ForeignKey(
        AssetClass, on_delete=models.CASCADE, blank=False, null=False
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name


class AssetClassInterest(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    type = models.IntegerField(blank=False, null=False)
    ac_id = models.CharField(max_length=32, blank=False, null=False)


class Geography(BaseModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    parent_id = models.CharField(max_length=32, blank=True, null=True, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name


class Listing(BaseModel):
    geography = models.ForeignKey(Geography, on_delete=models.PROTECT)
    sub_asset_class = models.ForeignKey(SubAssetClass, on_delete=models.PROTECT)
    impl_approach = models.CharField(max_length=100)
    fund_levr = models.FloatField(blank=True, null=True)
    fund_struc = models.CharField(max_length=100, blank=True, null=True)
    fund_inc_year = models.CharField(max_length=100, blank=True, null=True)
    fund_targ_clos_yr = models.CharField(max_length=100, blank=True, null=True)
    fund_vehi_type = models.CharField(max_length=100, blank=True, null=True)
    nav = models.FloatField()
    nav_dis_avl = models.FloatField(blank=True, null=True)
    expr_int_ddline = models.DateField()
    targ_irr = models.FloatField(blank=True, null=True)
    risk_prof = models.CharField(max_length=100)
    fund_ter = models.FloatField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    comments = models.TextField(max_length=1000)
    public = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)


class Tag(BaseModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    type = models.CharField(max_length=100, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)


class TagInstance(BaseModel):
    resource_id = models.CharField(max_length=32)
    resource_type = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=False, null=False)


class RegisterInterest(BaseModel):
    buyer_user = models.ForeignKey(User, on_delete=models.PROTECT)
    seller_user = models.ForeignKey(User, on_delete=models.PROTECT)
    listing = models.ForeignKey(User, on_delete=models.CASCADE)
    PERMISSION_OPTIONS = permissions_key_value_tuples()
    buyer_message_permissions = models.CharField(
        max_length=30, choices=PERMISSION_OPTIONS, default=DEFAULT_PERMISSION_KEY
    )
    seller_message_permissions = models.CharField(
        max_length=30, choices=PERMISSION_OPTIONS, default=DEFAULT_PERMISSION_KEY
    )
    STATUS_OPTIONS = message_options_tuple()
    status = models.CharField(
        max_length=30, choices=STATUS_OPTIONS, default=DEFAULT_MESSAGE_KEY
    )


class Message(BaseModel):
    message = models.TextField(max_length=1000)
    register_interest = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    last_edited_on = models.DateTimeField(blank=True, null=True, default=None)
