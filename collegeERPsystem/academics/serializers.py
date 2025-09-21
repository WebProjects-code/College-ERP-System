from rest_framework import serializers
from .models import Department, Program, Semester, Course, CourseOffering, Enrollment

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class CourseOfferingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOffering
        fields = "__all__"

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
        read_only_fields = ("enrolled_at",)
