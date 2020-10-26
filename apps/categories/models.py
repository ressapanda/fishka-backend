from django.db import models


class Category(models.Model):
    """
    Model describes every needed information for category.
    """

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=20, unique=True, help_text="Category for question")

    def __str__(self):
        return self.name

    @staticmethod
    def has_read_permission(request):
        return True

    # @allow_staff_or_superuser
    @staticmethod
    def has_write_permission(request):
        return True
