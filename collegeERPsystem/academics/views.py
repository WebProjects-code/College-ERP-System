from rest_framework import viewsets, filters
from .models import Department, Program, Semester, Course, CourseOffering, Enrollment
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated]

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["code","title"]

class CourseOfferingViewSet(viewsets.ModelViewSet):
    queryset = CourseOffering.objects.select_related("course","semester").prefetch_related("teachers")
    serializer_class = CourseOfferingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["semester","year","teachers"]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.select_related("student","offering")
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["offering","student","status"]
