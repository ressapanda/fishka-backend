import pytest
from rest_framework import status
from rest_framework.reverse import reverse_lazy
from rest_framework.test import APIClient, APITestCase

from apps.categories.factories import FrameworkCategoryFactory, LanguageCategoryFactory, TeamCategoryFactory
from apps.core.tests.utils import generate_dict_factory
from apps.questions.factories import QuestionFactory
from apps.questions.models import Question
from apps.questions.serializers import QuestionReadSerializer, QuestionSerializer


class QuestionViewsTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        super(QuestionViewsTestCase, cls).setUpTestData()

        cls.QuestionDictFactory = generate_dict_factory(QuestionFactory)

        cls.framework_category_1 = FrameworkCategoryFactory()
        cls.team_category_1 = TeamCategoryFactory()
        cls.language_category_1 = LanguageCategoryFactory()

        cls.question1 = QuestionFactory(is_public=True)
        QuestionFactory.create_batch(
            50, framework=cls.framework_category_1, team=cls.team_category_1, language=cls.language_category_1
        )
        QuestionFactory.create_batch(5, is_public=True)

    def setUp(self):
        self.client = APIClient()

    def test_question_list(self):
        """SHOULD get all questions"""
        response = self.client.get(reverse_lazy("questions-list"))
        questions_count = Question.objects.filter(is_public=True).count()
        response_count = len(response.data["results"])

        assert response.status_code == status.HTTP_200_OK
        assert response_count == questions_count

    def test_question_instance(self):
        """SHOULD get question instance"""
        response = self.client.get(reverse_lazy("questions-detail", kwargs={"pk": self.question1.pk}))
        question1 = QuestionReadSerializer(self.question1)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == question1.data

    @pytest.mark.django_db
    def test_question_create(self):
        """SHOULD create new question"""
        questions_count_before = Question.objects.all().count()
        question = self.QuestionDictFactory()
        question.pop("framework")
        question.pop("team")
        question.pop("language")
        response = self.client.post(reverse_lazy("questions-list"), data=question, format="json")
        questions_count_after = Question.objects.all().count()
        question1 = Question.objects.filter(question=question["question"]).first()
        question1_data = QuestionSerializer(question1)
        assert response.status_code == status.HTTP_201_CREATED
        assert questions_count_before + 1 == questions_count_after
        assert question1_data.data == response.data

    def test_question_bulk_create(self):
        """SHOULD create many questions at once"""
        questions_count_before = Question.objects.all().count()
        questions = [self.QuestionDictFactory() for _ in range(0, 9)]
        for question in questions:
            question.pop("framework")
            question.pop("team")
            question.pop("language")
        questions_added_count = len(questions)
        data = {"author_email": "test_mail@fishka.xyz.com", "questions": questions}
        response = self.client.post(reverse_lazy("questions-bulk-create"), data, format="json")
        questions_count_after = Question.objects.all().count()

        assert response.status_code == status.HTTP_201_CREATED
        assert questions_count_before + questions_added_count == questions_count_after

    def test_question_bulk_create_error(self):
        """SHOULD return validation error because of to many questions in request"""
        questions = [self.QuestionDictFactory() for _ in range(0, 20)]
        for question in questions:
            question.pop("framework")
            question.pop("team")
            question.pop("language")
        data = {"author_email": "test_mail@fishka.xyz.com", "questions": questions}
        response = self.client.post(reverse_lazy("questions-bulk-create"), data, format="json")

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_question_random_list(self):
        """SHOULD get random list of questions with default limit = 5"""
        response = self.client.get(reverse_lazy("questions-random-list"))
        response_count = len(response.data)

        assert response.status_code == status.HTTP_200_OK
        assert response_count == 5

    def test_question_random_list_limit(self):
        """SHOULD get random list of questions with custom limit = 1000"""
        response = self.client.get(reverse_lazy("questions-random-list") + "?limit=1000")
        response_count = len(response.data)
        questions_count = Question.objects.filter(is_public=True).count()

        assert response.status_code == status.HTTP_200_OK
        assert response_count == questions_count
