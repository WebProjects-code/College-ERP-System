from django.db import models
from academics.models import CourseOffering
from django.conf import settings

class Session(models.Model):
    offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, related_name="sessions")
    session_date = models.DateField()
    session_no = models.IntegerField()

class Record(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="records")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=[("present","present"),("absent","absent"),("late","late"),("excused","excused")], default="present")
