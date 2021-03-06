from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """
    Abstract base model providing dates of last update and create date.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"),
                                      help_text=_("Date when an object was created"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"),
                                      help_text=_("Date when an object was last updated"))

    class Meta:
        abstract = True
