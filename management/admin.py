from django.contrib import admin
from .models import Site,Configuration,Moderation

admin.site.register(
    [Site,Configuration,Moderation]
)
