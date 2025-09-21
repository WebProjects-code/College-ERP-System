import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "collegeERPsystem.settings")

app = Celery("erpapp")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
