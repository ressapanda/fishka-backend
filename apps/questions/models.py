from django.db import models

from apps.categories.models import Framework, Team, Language


class Question(models.Model):
    """
    Model describes every needed information for question.
    """

    class Meta:
        ordering = ['-updated_at']

    EASY = 'e'
    INTERMEDIATE = 'i'
    HARD = 'h'
    difficulty_choices = (
        (EASY, 'Easy'),
        (INTERMEDIATE, 'Intermediate'),
        (HARD, 'Hard'),
    )

    question = models.CharField(max_length=100, unique=True, help_text="Question title")
    answer = models.TextField(max_length=500, help_text="Question answer")
    difficulty = models.CharField(max_length=1, choices=difficulty_choices, db_index=True,
                                  help_text="Difficulty level of question")
    framework = models.ForeignKey(Framework, default=None, db_index=True, null=True, blank=True,
                                  on_delete=models.SET_NULL, help_text="Question framework category")
    team = models.ForeignKey(Team, default=None, db_index=True, null=True, blank=True, on_delete=models.SET_NULL,
                             help_text="Question team category")
    language = models.ForeignKey(Language, default=None, db_index=True, null=True, blank=True,
                                 on_delete=models.SET_NULL, help_text="Question language category")
    is_public = models.BooleanField(default=True, help_text="Field specifies if user can see question instance")
    author_email = models.EmailField(default=None, null=True, blank=True, help_text="Email address of question author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
