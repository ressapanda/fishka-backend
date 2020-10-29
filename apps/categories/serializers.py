from rest_framework.serializers import ModelSerializer

from apps.categories.models import Category


class CategoryReadSerializer(ModelSerializer):
    """
    Serializer for all categories from Framework/Team/Language
    """

    class Meta:
        model = Category
        fields = ["id", "name", "category_type"]
        read_only_fields = fields
