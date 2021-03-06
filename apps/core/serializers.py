from rest_framework import serializers


class StatisticsSerializer(serializers.Serializer):
    """
    Statistics serializer
    """
    questions_count = serializers.IntegerField(min_value=0, help_text="Number of publicated questions")
    categories_count = serializers.IntegerField(min_value=0, help_text="Number of categories")

    def create(self, validated_data: dict) -> None:
        raise NotImplementedError

    def update(self, instance: dict, validated_data: dict) -> None:
        raise NotImplementedError
