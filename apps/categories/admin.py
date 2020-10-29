from django.contrib import admin

from apps.categories.models import Language, Team, Framework

admin.site.register(Framework)
admin.site.register(Team)
admin.site.register(Language)
