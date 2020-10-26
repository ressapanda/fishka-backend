from django.db import models

from apps.categories.models import Category


class Question(models.Model):
    """
    Model describes every needed information for question.
    """

    class Meta:
        ordering = ['-updated_at']

    difficulty_choices = (
        ('easy', 'Easy'),
        ('intermediate', 'Intermediate'),
        ('hard', 'Hard'),
    )

    question = models.CharField(max_length=100, unique=True, help_text="Question title")
    answer = models.TextField(max_length=500, help_text="Question answer")
    categories = models.ManyToManyField(Category, db_index=True, help_text="Question categories")
    difficulty = models.CharField(max_length=20, choices=difficulty_choices, db_index=True,
                                  help_text="Difficulty level of question")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    def has_write_permission(request):
        return True
