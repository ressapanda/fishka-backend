import os

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from fishka_backend import settings

SchemaView = get_schema_view(
    openapi.Info(
        title="Fishka API",
        default_version='v0.1.0',
        description="Open api information on fishka backend",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="MIT License"),
    ),
    url=f'https://{os.environ.get("URL", "localhost")}/',
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_patterns = [
    path("docs/", SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),

    path("core/", include("apps.core.urls")),
    path("questions/", include("apps.questions.urls")),
    path("categories/", include("apps.categories.urls")),
]

urlpatterns = [
    path("api/", include(api_patterns)),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
