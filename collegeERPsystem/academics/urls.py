from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, ProgramViewSet, SemesterViewSet, CourseViewSet, CourseOfferingViewSet, EnrollmentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("departments", DepartmentViewSet)
router.register("programs", ProgramViewSet)
router.register("semesters", SemesterViewSet)
router.register("courses", CourseViewSet)
router.register("offerings", CourseOfferingViewSet)
router.register("enrollments", EnrollmentViewSet)

urlpatterns = [path("", include(router.urls))]
