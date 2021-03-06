from django.contrib import admin, messages
from django.http import HttpRequest
from django.utils.translation import ngettext
from django.db.models import QuerySet
from apps.questions.models import Question


class QuestionAdmin(admin.ModelAdmin):
    """Admin model for question category."""

    list_display = ['__str__', 'difficulty', 'framework', 'team', 'language']
    list_filter = ['difficulty', 'framework', 'team', 'language']

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        qs = super().get_queryset(request)
        return qs.filter(is_public=True)


class QuestionSuggestionAdmin(admin.ModelAdmin):
    """Admin model for question suggestion category."""

    list_display = ['__str__', 'author_email', 'created_at']
    ordering = ['created_at']
    actions = ['make_published']

    def get_queryset(self, request: HttpRequest) -> QuerySet:
        qs = super().get_queryset(request)
        return qs.filter(is_public=False)

    def make_published(self, request: HttpRequest, queryset: QuerySet) -> None:
        updated = queryset.update(is_public=True)
        self.message_user(request, ngettext(
            '%d question was successfully marked as published.',
            '%d questions were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    make_published.short_description = "Mark selected questions as published"  # type: ignore


class QuestionSuggestion(Question):
    class Meta:
        proxy = True


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionSuggestion, QuestionSuggestionAdmin)
