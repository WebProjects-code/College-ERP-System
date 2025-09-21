from rest_framework import viewsets
from .models import Assignment, Submission, GradeItem, Mark
from .serializers import *

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class GradeItemViewSet(viewsets.ModelViewSet):
    queryset = GradeItem.objects.all()
    serializer_class = GradeItemSerializer

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
