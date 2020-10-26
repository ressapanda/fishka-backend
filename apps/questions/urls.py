from rest_framework import routers

from apps.questions.views import QuestionViewSet

router = routers.SimpleRouter()

router.register(r"", QuestionViewSet, "questions")

urlpatterns = router.urls
