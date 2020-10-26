from rest_framework.serializers import ModelSerializer

from apps.categories.models import Category


class CategorySerializer(ModelSerializer):
    """
    Category model serializer
    """

    class Meta:
        model = Category
        fields = ["id", "name"]
        read_only_fields = ["id"]


class CategoryReadSerializer(ModelSerializer):
    """
    Category model read only serializer
    """

    class Meta:
        model = Category
        fields = ["id", "name"]
        read_only_fields = fields
