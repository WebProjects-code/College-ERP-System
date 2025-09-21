from rest_framework import serializers
from .models import Assignment, Submission, GradeItem, Mark

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"
        read_only_fields = ("student","submitted_at","status")

class GradeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeItem
        fields = "__all__"

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = "__all__"
        read_only_fields = ("graded_at",)
