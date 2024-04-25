from django.db import models
from users.models import Cususer


# model for project
class Project(models.Model):
    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    objective = models.TextField()
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Not Started')
    deadline = models.DateField()

    def __str__(self):
        return self.name 
    
class ProjectEmployee(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Cususer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'employee')

    def __str__(self):
        return f'{self.project.name} - {self.employee.name}'