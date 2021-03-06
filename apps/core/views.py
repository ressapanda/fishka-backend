from typing import Union, Dict, Any

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import SerializerMetaclass

from apps.categories.models import Category
from apps.core.serializers import StatisticsSerializer
from apps.questions.models import Question


class MultiSerializerMixin:  # pylint:disable=too-few-public-methods
    """
    Get specified serializer from array.
    """
    serializers: Dict[str, Union[None, SerializerMetaclass]] = {
        'default': None,
    }

    def get_serializer_class(self) -> Any:
        """
        Function get serializer for every specific action

        :return: Serializer described in serializers dict
        """
        try:
            serializer_class = self.serializers[self.action]  # type: ignore
        except KeyError:
            serializer_class = self.serializers['default']
        return serializer_class


@api_view(['get'])
def get_statistics(request: Request) -> Response:
    """
    List number of questions and categories

    View to list questions and categories count.
    """
    data = {
        "questions_count": Question.objects.filter(is_public=True).count(),
        "categories_count": Category.objects.all().count(),
    }
    serializer = StatisticsSerializer(data)
    return Response(serializer.data)
