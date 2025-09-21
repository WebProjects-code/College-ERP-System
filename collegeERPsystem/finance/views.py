from rest_framework import viewsets
from .models import FeePlan, FeeInvoice, Payment
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response

class FeePlanViewSet(viewsets.ModelViewSet):
    queryset = FeePlan.objects.all()
    serializer_class = FeePlanSerializer

class FeeInvoiceViewSet(viewsets.ModelViewSet):
    queryset = FeeInvoice.objects.all()
    serializer_class = FeeInvoiceSerializer

    @action(detail=False, methods=["post"])
    def generate(self, request):
        # expected: student_id, semester_id
        student_id = request.data.get("student_id")
        semester_id = request.data.get("semester_id")
        # simple generation: find feeplan by student's program? simplified
        from django.shortcuts import get_object_or_404
        student = get_object_or_404(settings.AUTH_USER_MODEL, id=student_id)
        # This is an example stub: production code should snapshot fee details.
        invoice = FeeInvoice.objects.create(student_id=student_id, semester_id=semester_id, amount=10000, due_date="2099-12-31")
        return Response(FeeInvoiceSerializer(invoice).data)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=True, methods=["post"])
    def mark_success(self, request, pk=None):
        obj = self.get_object()
        txn = request.data.get("txn_id")
        obj.mark_success(txn)
        return Response(self.get_serializer(obj).data)
