from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("notifications", NotificationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
