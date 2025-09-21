from rest_framework import serializers
from .models import Session, Record

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"
