from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from meltexapp.models import User, Company

class UserAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
