from django.db import models
from django.conf import settings

class Department(models.Model):
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

class Program(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="programs")
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=16)
    duration_semesters = models.IntegerField(default=8)

    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Course(models.Model):
    code = models.CharField(max_length=16, unique=True)
    title = models.CharField(max_length=256)
    credits = models.DecimalField(max_digits=4, decimal_places=1, default=3.0)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} - {self.title}"

class CourseOffering(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    section = models.CharField(max_length=8, default="A")
    year = models.IntegerField()
    teachers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="offerings")
    capacity = models.IntegerField(default=30)

    def __str__(self):
        return f"{self.course.code} - {self.semester.name} {self.section}"

class Enrollment(models.Model):
    STATUS_CHOICES = (("active","active"),("dropped","dropped"),("completed","completed"))
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enrollments")
    offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, related_name="enrollments")
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="active")
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student","offering")

    def __str__(self):
        return f"{self.student.email} -> {self.offering}"
