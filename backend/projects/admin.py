from django.contrib import admin
from .models import Project
from .models import ProjectEmployee
from .models import EmployeeAnswer

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectEmployee)
admin.site.register(EmployeeAnswer)

