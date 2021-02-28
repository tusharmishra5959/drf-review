from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Profile


class ProfileAdmin(ModelAdmin):
    """."""

    readonly_fields = ("id",)


admin.site.register(Profile, ProfileAdmin)
