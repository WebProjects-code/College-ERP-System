from django.db import models
from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    type = models.CharField(max_length=64, default="announcement")
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class AuditLog(models.Model):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=64)
    target_type = models.CharField(max_length=128, null=True, blank=True)
    target_id = models.IntegerField(null=True, blank=True)
    diff = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
