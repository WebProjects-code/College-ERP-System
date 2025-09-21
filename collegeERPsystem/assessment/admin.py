from django.contrib import admin
from .models import Assignment, Submission, GradeItem, Mark
# Register your models here.
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(GradeItem)
admin.site.register(Mark)