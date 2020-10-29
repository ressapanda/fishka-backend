from django.db import models


class Category(models.Model):
    """
    Abstract model for category name.
    """

    class Meta:
        ordering = ['name']

    FRAMEWORK = 'framework'
    TEAM = 'team'
    LANGUAGE = 'language'
    category_type_choices = (
        (FRAMEWORK, 'Framework'),
        (TEAM, 'Team'),
        (LANGUAGE, 'Language'),
    )

    name = models.CharField(max_length=20, unique=True, help_text="Category name")
    category_type = models.CharField(choices=category_type_choices, max_length=9, editable=False,
                                     help_text="Category type")

    def __str__(self):
        return self.name


class Framework(Category):
    """
    Model contains categories.
    """

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.category_type = Category.FRAMEWORK
        super().save(force_insert, force_update, using, update_fields)


class Team(Category):
    """
    Model contains categories about work group name.
    """

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.category_type = Category.TEAM
        super().save(force_insert, force_update, using, update_fields)


class Language(Category):
    """
    Model contains categories about programming language.
    """

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.category_type = Category.LANGUAGE
        super().save(force_insert, force_update, using, update_fields)
