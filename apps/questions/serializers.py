from typing import List

from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed, ValidationError
from rest_framework.serializers import ModelSerializer, Serializer

from apps.categories.serializers import FrameworkReadSerializer, TeamReadSerializer, \
    LanguageReadSerializer
from apps.questions.models import Question


class QuestionSerializer(ModelSerializer):
    """
    Question model serializer
    """

    class Meta:
        model = Question
        fields = ["id", "question", "answer", "difficulty", "framework", "team", "language", "author_email"]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> Question:
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
    framework = FrameworkReadSerializer(read_only=True)
    team = TeamReadSerializer(read_only=True)
    language = LanguageReadSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ["id", "question", "answer", "difficulty", "framework", "team", "language", "created_at", "updated_at"]
        read_only_fields = fields


class BulkCreateQuestionSerializer(ModelSerializer):
    """
    Serializer used for bulk create questions list
    """

    class Meta:
        model = Question
        fields = ["id", "question", "answer", "difficulty", "framework", "team", "language", "author_email"]
        read_only_fields = ["id", "author_email"]


class BulkCreateQuestionsSerializer(Serializer):
    """
    Serializer for bulk create method
    """
    author_email = serializers.EmailField(required=True, help_text="Email address of question author")
    questions = BulkCreateQuestionSerializer(many=True)

    class Meta:
        fields = ["author_email", "questions"]

    @staticmethod
    def validate_questions(value: list) -> list:
        """
        Validator for questions to check questions length
        """
        if len(value) >= 10:
            raise ValidationError("You can send only 10 questions in one request.")
        return value

    @transaction.atomic
    def create(self, validated_data: dict) -> dict:
        """
        Custom create function with handling bulk create.

        :param validated_data: serializer data after validation
        :return: created list of Question objects
        """
        author_email = validated_data['author_email']
        questions = validated_data.pop('questions')
        validated_data['questions'] = []
        for question in questions:
            validated_data['questions'].append(Question.objects.create(
                **question,
                is_public=False,
                author_email=author_email
            ))
        return validated_data

    def update(self, instance: Question, validated_data: dict) -> None:
        raise MethodNotAllowed
