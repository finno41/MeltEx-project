from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from meltexapp.models import User

class UserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(User, UserAdmin)
