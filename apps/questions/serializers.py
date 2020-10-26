from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.categories.models import Category
from apps.questions.models import Question


class QuestionSerializer(ModelSerializer):
    """
    Question model serializer
    """
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all(),
                                                    help_text="List of category id's")

    class Meta:
        model = Question
        fields = ["id", "question", "answer", "categories", "difficulty", "created_at", "updated_at"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        """
        Custom create function with handling of nested objects.

        :param validated_data: serializer data after validation
        :return: created Question object
        """
        categories = validated_data.pop('categories', [])
        question = Question.objects.create(**validated_data)

        question.categories.set(categories)

        question.refresh_from_db()
        return question

    def update(self, instance, validated_data):
        """
        Custom update function with handling of nested objects.

        :param instance: updated Question object instance
        :param validated_data: serializer data after validation
        :return: updated Question object
        """
        categories = validated_data.pop('categories', None)

        instance = super().update(instance, validated_data)

        if categories is not None:
            instance.categories.set(categories)

        instance.refresh_from_db()
        return instance


class QuestionReadSerializer(ModelSerializer):
    """
    Question model read only serializer
    """

    class Meta:
        model = Question
        fields = ["id", "question", "answer", "categories", "difficulty", "created_at", "updated_at"]
        read_only_fields = fields
