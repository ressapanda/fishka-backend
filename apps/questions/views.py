from django_filters.rest_framework import DjangoFilterBackend
from dry_rest_permissions.generics import DRYPermissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from apps.core.views import MultiSerializerMixin
from apps.questions.models import Question
from apps.questions.serializers import QuestionReadSerializer, QuestionSerializer


class QuestionViewSet(MultiSerializerMixin, ModelViewSet):
    """
        ViewSet based on Question model.

        list: List every Question.

        ### This route allow to:
         - Filter by field: *'categories', 'difficulty'*
         - Order by field: *'id', 'created_at', 'updated_at'*
         - Search fraze used in fields: *'question'*

        retrieve: Retrieve specific instance of question.

        To correct response you need provide *id* of existing question instance in path.

        update: Update question instance informations.

        To correct response you need provide *id* of existing question instance in path.

        create: Create new question.

        To successfuly add new question check QuestionSerializer for needed fields and its additional parameters.

        partial_update: Patch question.

        To correct response you need provide *id* of existing question instance in path.

        destroy: Delete question.

        To correct response you need provide *id* of existing question instance in path.
        """
    permission_classes = (DRYPermissions,)
    queryset = Question.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ['categories', 'difficulty']
    ordering_fields = ['id', 'created_at', 'updated_at']
    search_fields = ['question']

    serializers = {
        'create': QuestionSerializer,
        'update': QuestionSerializer,
        'partial_update': QuestionSerializer,
        'default': QuestionReadSerializer
    }
