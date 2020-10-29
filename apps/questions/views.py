from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import GenericViewSet

from apps.core.views import MultiSerializerMixin
from apps.questions.models import Question
from apps.questions.serializers import QuestionReadSerializer, QuestionSerializer


class QuestionViewSet(MultiSerializerMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    """
        ViewSet based on Question model.

        list: List every Question.

        ### This route allow to:
         - Filter by field: *'categories', 'difficulty'*
         - Order by field: *'id', 'created_at', 'updated_at'*
         - Search fraze used in fields: *'question'*

        retrieve: Retrieve specific instance of question.

        To correct response you need provide *id* of existing question instance in path.

        create: Create new question.

        To successfuly add new question check QuestionSerializer.
        """
    queryset = Question.objects.filter(is_public=True)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ['framework', 'team', 'language', 'difficulty']
    ordering_fields = ['id', 'created_at', 'updated_at']
    search_fields = ['question']

    serializers = {
        'create': QuestionSerializer,
        'default': QuestionReadSerializer
    }
