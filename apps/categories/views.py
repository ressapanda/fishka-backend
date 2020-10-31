from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.categories.models import Category
from apps.categories.serializers import CategoryReadSerializer, CategoryQuestionsCountSerializer
from apps.core.views import MultiSerializerMixin


class CategoryViewSet(MultiSerializerMixin,
                      ReadOnlyModelViewSet):
    """
    ViewSet based on Category model.

    list: List every Category.

    This route doesn't allow to filter,search or order requests.

    retrieve: Retrieve specific instance of category.
    """
    queryset = Category.objects.all()

    serializers = {
        'questions_count': CategoryQuestionsCountSerializer,
        'default': CategoryReadSerializer
    }

    @action(detail=False, methods=['get'])
    def questions_count(self, request):
        """
        Returns categories with questions count.

        :param request: request object
        :return: List of categories
        """
        return super().list(request)
