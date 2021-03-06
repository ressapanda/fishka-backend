from typing import Any

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    """Abstract model for category name."""

    class CategoryType(models.TextChoices):
        FRAMEWORK = 'framework', _('Framework')
        TEAM = 'team', _('Team')
        LANGUAGE = 'language', _('Language')

    name = models.CharField(max_length=20, unique=True, verbose_name=_("Name"), help_text=_("Category name"))
    category_type = models.CharField(choices=CategoryType.choices, max_length=9, editable=False,
                                     verbose_name=_("Category type"), help_text=_("Category type"))

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Framework(Category):
    """Model contains categories."""

    def save(self, force_insert: bool = False, force_update: bool = False, using: Any = None,
             update_fields: Any = None) -> None:
        self.category_type = Category.CategoryType.FRAMEWORK
        super().save(force_insert, force_update, using, update_fields)


class Team(Category):
    """Model contains categories about work group name."""

    def save(self, force_insert: bool = False, force_update: bool = False, using: Any = None,
             update_fields: Any = None) -> None:
        self.category_type = Category.CategoryType.TEAM
        super().save(force_insert, force_update, using, update_fields)


class Language(Category):
    """Model contains categories about programming language."""

    def save(self, force_insert: bool = False, force_update: bool = False, using: Any = None,
             update_fields: Any = None) -> None:
        self.category_type = Category.CategoryType.LANGUAGE
        super().save(force_insert, force_update, using, update_fields)
