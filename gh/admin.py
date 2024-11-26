from django.contrib import admin
from gh.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile)
