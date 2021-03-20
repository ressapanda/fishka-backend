import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.categories.models import Category, Framework, Language, Team


class CategoryFactory(DjangoModelFactory):
    """Category model factory for tests purpose."""

    name = factory.Sequence(lambda n: f"category-{n}")
    category_type = factory.fuzzy.FuzzyChoice(("Framework", "Team", "Language"))

    class Meta:
        model = Category


class FrameworkCategoryFactory(DjangoModelFactory):
    """Framework category model factory for tests purpose."""

    name = factory.Sequence(lambda n: f"category-framework-{n}")
    category_type = Category.CategoryType.FRAMEWORK

    class Meta:
        model = Framework


class TeamCategoryFactory(DjangoModelFactory):
    """Team category model factory for tests purpose."""

    name = factory.Sequence(lambda n: f"category-team-{n}")
    category_type = Category.CategoryType.TEAM

    class Meta:
        model = Team


class LanguageCategoryFactory(DjangoModelFactory):
    """Language category model factory for tests purpose."""

    name = factory.Sequence(lambda n: f"category-language-{n}")
    category_type = Category.CategoryType.LANGUAGE

    class Meta:
        model = Language
