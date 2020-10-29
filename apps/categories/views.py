from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.categories.models import Category
from apps.categories.serializers import CategoryReadSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    """
    ViewSet based on Category model.

    list: List every Category.

    This route doesn't allow to filter,search or order requests.

    retrieve: Retrieve specific instance of category.
    """
    queryset = Category.objects.all()
    serializer_class = CategoryReadSerializer
