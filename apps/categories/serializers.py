from rest_framework.serializers import ModelSerializer

from apps.categories.models import Category, Framework, Team, Language


class CategoryReadSerializer(ModelSerializer):
    """
    Serializer for all categories from Framework/Team/Language
    """

    class Meta:
        model = Category
        fields = ["id", "name", "category_type"]
        read_only_fields = fields


class FrameworkReadSerializer(ModelSerializer):
    """
    Framework read serializer
    """

    class Meta:
        model = Framework
        fields = ["id", "name"]
        read_only_fields = fields


class TeamReadSerializer(ModelSerializer):
    """
    Team read serializer
    """

    class Meta:
        model = Team
        fields = ["id", "name"]
        read_only_fields = fields


class LanguageReadSerializer(ModelSerializer):
    """
    Language read serializer
    """

    class Meta:
        model = Language
        fields = ["id", "name"]
        read_only_fields = fields
