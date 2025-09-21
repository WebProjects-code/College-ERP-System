from django.contrib import admin
from .models import Notification, AuditLog
# Register your models here.
admin.site.register(Notification)
admin.site.register(AuditLog)