from rest_framework.routers import DefaultRouter
from .views import AssignmentViewSet, SubmissionViewSet, GradeItemViewSet, MarkViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("assignments", AssignmentViewSet)
router.register("submissions", SubmissionViewSet)
router.register("grade-items", GradeItemViewSet)
router.register("marks", MarkViewSet)

urlpatterns = [path("", include(router.urls))]
