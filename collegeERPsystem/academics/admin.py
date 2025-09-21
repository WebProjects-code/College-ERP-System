from django.contrib import admin
from .models import Department, Program, Semester, Course, CourseOffering,Enrollment

# Register your models here.
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(CourseOffering)
admin.site.register(Enrollment)

