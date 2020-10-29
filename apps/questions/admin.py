from django.contrib import admin

from apps.questions.models import Question


class QuestionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_public=True)


class QuestionSuggestionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_public=False)


class QuestionSuggestion(Question):
    class Meta:
        proxy = True


admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionSuggestion, QuestionSuggestionAdmin)
