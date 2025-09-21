from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("rest_framework_simplejwt.views")),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/v1/accounts/", include("accounts.urls")),
    path("api/v1/academics/", include("academics.urls")),
    path("api/v1/assessment/", include("assessment.urls")),
    path("api/v1/attendance/", include("attendance.urls")),
    path("api/v1/finance/", include("finance.urls")),
    path("api/v1/notifications/", include("notifications.urls")),
]
