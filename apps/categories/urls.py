from rest_framework import routers

from apps.categories.views import CategoryViewSet

router = routers.SimpleRouter()

router.register(r"", CategoryViewSet, "categories")

urlpatterns = router.urls
