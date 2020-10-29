from rest_framework.serializers import ModelSerializer

from apps.questions.models import Question


class QuestionSerializer(ModelSerializer):
    """
    Question model serializer
    """

    class Meta:
        model = Question
        fields = ["id", "question", "answer", "difficulty", "framework", "team", "language", "author_email"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        """
        Custom create function with handling of nested objects.

        :param validated_data: serializer data after validation
        :return: created Question object
        """
        question = Question.objects.create(**validated_data, is_public=False)
        return question


class QuestionReadSerializer(ModelSerializer):
    """
    Question model read only serializer
    """

    class Meta:
        model = Question
        fields = ["id", "question", "answer", "difficulty", "framework", "team", "language", "created_at", "updated_at"]
        read_only_fields = fields
