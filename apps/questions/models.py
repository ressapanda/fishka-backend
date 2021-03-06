from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.categories.models import Framework, Team, Language
from apps.core.models import BaseModel


class Question(BaseModel):
    """
    Model describes every needed information for question.
    """

    class Difficulty(models.TextChoices):
        EASY = 'e', _('Easy')
        INTERMEDIATE = 'i', _('Intermediate')
        HARD = 'h', _('Hard')

    question = models.CharField(max_length=100, unique=True, verbose_name=_("Question"), help_text=_("Question title"))
    answer = models.TextField(max_length=500, verbose_name=_("Answer"), help_text=_("Question answer"))
    difficulty = models.CharField(max_length=1, choices=Difficulty.choices, db_index=True, verbose_name=_("Difficulty"),
                                  help_text=_("Difficulty level of question"))
    framework = models.ForeignKey(Framework, default=None, db_index=True, null=True, blank=True,
                                  related_name="questions", on_delete=models.SET_NULL,
                                  verbose_name=_("Framework category"), help_text=_("Question framework category"))
    team = models.ForeignKey(Team, default=None, db_index=True, null=True, blank=True, on_delete=models.SET_NULL,
                             related_name="questions", verbose_name=_("Team category"),
                             help_text=_("Question team category"))
    language = models.ForeignKey(Language, default=None, db_index=True, null=True, blank=True, related_name="questions",
                                 on_delete=models.SET_NULL, verbose_name=_("Language category"),
                                 help_text=_("Question language category"))
    is_public = models.BooleanField(default=True, verbose_name=_("Is public"),
                                    help_text=_("Field specifies if user can see question instance"))
    author_email = models.EmailField(default=None, null=True, blank=True, verbose_name=_("Author email"),
                                     help_text=_("Email address of question author"))

    class Meta:
        ordering = ['-updated_at']
