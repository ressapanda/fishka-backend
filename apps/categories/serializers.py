from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.categories.models import Category, Framework, Language, Team


class CategoryReadSerializer(ModelSerializer):
    """Serializer for all categories from Framework/Team/Language."""

    class Meta:
        model = Category
        fields = ["id", "name", "category_type"]
        read_only_fields = fields


class CategoryQuestionsCountSerializer(ModelSerializer):
    """Serializer for category list with count of questions."""

    questions_count = SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "category_type", "questions_count"]
        read_only_fields = fields

    @staticmethod
    def get_questions_count(obj: Category) -> int:
        """
        Return amount of questions in specific category type.

        :return: Amount of questions in category
        """
        if obj.category_type == "framework":
            return obj.framework.questions.all().filter(is_public=True).count()
        if obj.category_type == "team":
            return obj.team.questions.all().filter(is_public=True).count()
        if obj.category_type == "language":
            return obj.language.questions.all().filter(is_public=True).count()
        return 0


class FrameworkReadSerializer(ModelSerializer):
    """Framework read serializer."""

    class Meta:
        model = Framework
        fields = ["id", "name"]
        read_only_fields = fields


class TeamReadSerializer(ModelSerializer):
    """Team read serializer."""

    class Meta:
        model = Team
        fields = ["id", "name"]
        read_only_fields = fields


class LanguageReadSerializer(ModelSerializer):
    """Language read serializer."""

    class Meta:
        model = Language
        fields = ["id", "name"]
        read_only_fields = fields
