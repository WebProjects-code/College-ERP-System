from rest_framework import serializers
from .models import FeePlan, FeeInvoice, Payment

class FeePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeePlan
        fields = "__all__"

class FeeInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeInvoice
        fields = "__all__"
        read_only_fields = ("generated_at",)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
