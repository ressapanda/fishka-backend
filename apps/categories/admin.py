from django.contrib import admin

from apps.categories.models import Framework, Language, Team

admin.site.register(Framework)
admin.site.register(Team)
admin.site.register(Language)
