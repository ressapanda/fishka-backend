from django.urls import path

from apps.core.views import get_statistics

urlpatterns = [
    path('statistics/', get_statistics)
]
