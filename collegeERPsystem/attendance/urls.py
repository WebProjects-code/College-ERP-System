from rest_framework.routers import DefaultRouter
from .views import SessionViewSet, RecordViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("sessions", SessionViewSet)
router.register("records", RecordViewSet)

urlpatterns = [path("", include(router.urls))]
