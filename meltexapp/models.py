from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import uuid

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=50, blank=False, null=False)
    type = models.TextField(max_length=50, blank=False, null=False)
    # subscriber = models.BooleanField(default=False)

class User(AbstractUser):
    phone_number = models.TextField(max_length=20, blank=True)
    # interested_acs = linked to acs
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)

class Listing(models.Models):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_class_name = models.CharField(max_length=100)
    sub_asset_class_name = models.CharField(max_length=100)
    geography = models.CharField(max_length=100)
    impl_approach = models.CharField(max_length=100)
    fund_levr = models.CharField(max_length=100)
    fund_struc = models.CharField(max_length=100)
    fund_inc_year = models.CharField(max_length=100)
    fund_targ_clos_yr = models.CharField(max_length=100)
    fund_vehi_type = models.CharField(max_length=100)
    nav = models.CharField(max_length=100)
    nav_dis_avl = models.CharField(max_length=100)
    expr_int_ddline = models.CharField(max_length=100)
    targ_irr = models.CharField(max_length=100)
    risk_prof = models.CharField(max_length=100)
    fund_ter = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    comments = models.TextField(max_length=1000)

class Tag(models.model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    type = models.CharField(max_length=100, blank=False, null=False)

class TagInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    resource_id = models.CharField(max_length=32)
    resource_type = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=False, null=False)
