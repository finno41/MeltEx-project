from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import NOT_PROVIDED
import uuid
from datetime import datetime


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=50, blank=False, null=False)
    type = models.TextField(max_length=50, blank=False, null=False)


class User(AbstractUser):
    phone_number = models.TextField(max_length=20, blank=True, null=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, blank=True, null=True
    )
    subscriber = models.BooleanField(default=False)


class AssetClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)


class SubAssetClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    asset_class = models.ForeignKey(
        AssetClass, on_delete=models.CASCADE, blank=False, null=False
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)


class AssetClassInterest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    type = models.IntegerField(blank=False, null=False)
    ac_id = models.CharField(max_length=32, blank=False, null=False)


class Geography(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    parent_id = models.CharField(max_length=32, blank=True, null=True, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.name


class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    geography = models.ForeignKey(
        Geography, on_delete=models.CASCADE, blank=False, null=False
    )
    sub_asset_class = models.ForeignKey(
        SubAssetClass, on_delete=models.CASCADE, blank=False, null=False
    )
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    comments = models.TextField(max_length=1000)
    public = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=datetime.now())
    updated_on = models.DateTimeField(default=datetime.now())
    deleted_on = models.DateTimeField(blank=True, null=True)


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    type = models.CharField(max_length=100, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)


class TagInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resource_id = models.CharField(max_length=32)
    resource_type = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=False, null=False)
