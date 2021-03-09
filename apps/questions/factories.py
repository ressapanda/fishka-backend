import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.categories.factories import FrameworkCategoryFactory, TeamCategoryFactory, LanguageCategoryFactory
from apps.questions.models import Question


class QuestionFactory(DjangoModelFactory):
    """Question model factory for tests purpose."""
    question = factory.Sequence(lambda n: f"question-question-{n}")
    answer = factory.Sequence(lambda n: f"question-answer-{n}")
    difficulty = factory.fuzzy.FuzzyChoice(("e", "i", "h"))
    framework = factory.SubFactory(FrameworkCategoryFactory)
    team = factory.SubFactory(TeamCategoryFactory)
    language = factory.SubFactory(LanguageCategoryFactory)
    is_public = factory.fuzzy.FuzzyChoice((True, False))
    author_email = factory.Faker("email", locale="PL")

    class Meta:
        model = Question
