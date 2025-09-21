from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    ADMIN = "admin", "Admin"
    TEACHER = "teacher", "Teacher"
    STUDENT = "student", "Student"

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=16, choices=Role.choices, default=Role.STUDENT)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"
