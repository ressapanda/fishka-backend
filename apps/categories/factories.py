import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.categories.models import Category, Language, Team, Framework


class CategoryFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"category-{n}")
    category_type = factory.fuzzy.FuzzyChoice(("Framework", "Team", "Language"))

    class Meta:
        model = Category


class FrameworkCategoryFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"category-framework-{n}")
    category_type = "Framework"

    class Meta:
        model = Framework


class TeamCategoryFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"category-team-{n}")
    category_type = "Team"

    class Meta:
        model = Team


class LanguageCategoryFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: f"category-language-{n}")
    category_type = "Language"

    class Meta:
        model = Language
