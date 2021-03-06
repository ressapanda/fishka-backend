from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.categories.models import Category
from apps.categories.serializers import CategoryReadSerializer, CategoryQuestionsCountSerializer
from apps.core.views import MultiSerializerMixin


class CategoryViewSet(MultiSerializerMixin,
                      ReadOnlyModelViewSet):
    """
    ViewSet based on Category model.

    list: List every Category.

    ### This route allow to:
        - Filter by field: *'category_type'*

    retrieve: Retrieve specific instance of category.
    """

    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['category_type']

    serializers = {
        'questions_count': CategoryQuestionsCountSerializer,
        'default': CategoryReadSerializer
    }

    @action(detail=False, methods=['get'])
    def questions_count(self, request: Request) -> Response:
        """
        Return categories with questions count.

        :param request: request object
        :return: List of categories
        """
        return super().list(request)
