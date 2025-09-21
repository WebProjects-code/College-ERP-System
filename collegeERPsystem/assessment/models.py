from django.db import models
from django.conf import settings
from academics.models import CourseOffering

class Assignment(models.Model):
    offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, related_name="assignments")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    total_marks = models.IntegerField(default=100)
    due_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to="submissions/", null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=16, choices=[("submitted","submitted"),("graded","graded"),("late","late")], default="submitted")

class GradeItem(models.Model):
    offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, related_name="grade_items")
    name = models.CharField(max_length=128)
    weight_percent = models.DecimalField(max_digits=5, decimal_places=2)

class Mark(models.Model):
    grade_item = models.ForeignKey(GradeItem, on_delete=models.CASCADE, related_name="marks")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=6, decimal_places=2)
    graded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="graded_marks")
    graded_at = models.DateTimeField(auto_now=True)
