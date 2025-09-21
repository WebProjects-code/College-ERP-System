from rest_framework.routers import DefaultRouter
from .views import FeePlanViewSet, FeeInvoiceViewSet, PaymentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register("fee-plans", FeePlanViewSet)
router.register("invoices", FeeInvoiceViewSet, basename="invoices")
router.register("payments", PaymentViewSet)

urlpatterns = [path("", include(router.urls))]
