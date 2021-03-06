from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.core.views import MultiSerializerMixin
from apps.questions.models import Question
from apps.questions.serializers import BulkCreateQuestionsSerializer, QuestionReadSerializer, QuestionSerializer


class QuestionViewSet(
    MultiSerializerMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet
):
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
    filter_fields = ["framework", "team", "language", "difficulty"]
    ordering_fields = ["id", "created_at", "updated_at"]
    search_fields = ["question"]

    serializers = {
        "bulk_create": BulkCreateQuestionsSerializer,
        "create": QuestionSerializer,
        "default": QuestionReadSerializer,
    }

    @action(detail=False, methods=["post"])
    def bulk_create(self, request: Request) -> Response:
        """
        Create many questions in on request.

        :param request: request object
        :return: List of created questions
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["get"])
    def random_list(self, request: Request) -> Response:
        """
        Return random list of questions.

        :param request: request object
        :return: List of random questions
        """
        queryset = self.filter_queryset(self.get_queryset())
        limit = int(request.query_params.get("limit", 5))
        count = queryset.count()
        if count > limit:
            queryset = queryset.order_by("?")[:limit]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
