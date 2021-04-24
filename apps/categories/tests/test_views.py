from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient, APITestCase

from apps.categories.factories import (
    CategoryFactory,
    FrameworkCategoryFactory,
    LanguageCategoryFactory,
    TeamCategoryFactory,
)
from apps.categories.models import Category
from apps.categories.serializers import CategoryReadSerializer
from apps.questions.factories import QuestionFactory


class CategoryViewsTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super(CategoryViewsTestCase, cls).setUpTestData()

        cls.category1 = CategoryFactory()
        FrameworkCategoryFactory.create_batch(10)
        TeamCategoryFactory.create_batch(10)
        LanguageCategoryFactory.create_batch(10)
        QuestionFactory.create_batch(20)

    def setUp(self):
        self.client = APIClient()

    def test_category_list(self):
        """SHOULD get all categories"""
        response = self.client.get(reverse_lazy("categories-list"))
        categories_count = Category.objects.all().count()
        response_count = len(response.data["results"])

        assert response.status_code == status.HTTP_200_OK
        assert response_count == categories_count

    def test_category_instance(self):
        """SHOULD get category instance"""
        response = self.client.get(reverse_lazy("categories-detail", kwargs={"pk": self.category1.pk}))
        category1 = CategoryReadSerializer(self.category1)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == category1.data

    def test_category_list_questions_count(self):
        """SHOULD get all categories with questions counter"""
        response = self.client.get(reverse_lazy("categories-questions-count"))
        categories_count = Category.objects.all().count()
        response_count = len(response.data["results"])

        assert response.status_code == status.HTTP_200_OK
        assert response_count == categories_count
