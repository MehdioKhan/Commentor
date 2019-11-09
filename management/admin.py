from django.contrib import admin
from .models import Site,Configuration,ModerationSetting

admin.site.register(
    [Site,Configuration,ModerationSetting]
)
