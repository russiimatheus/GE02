from django.contrib import admin
from .models import Portfolio, Student, Project  # Ensure you import Project here

# Register your models here.
admin.site.register(Student)
admin.site.register(Portfolio)
admin.site.register(Project)  # Register the Project model

