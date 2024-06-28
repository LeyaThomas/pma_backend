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
    
class EmployeeAnswer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Cususer, on_delete=models.CASCADE)
    mark = models.IntegerField(default=0)
    question1 = models.BooleanField(default=False)
    question2 = models.BooleanField(default=False)
    question3 = models.BooleanField(default=False)
    question4 = models.BooleanField(default=False)
    question5 = models.BooleanField(default=False)

    def calculate_mark(self):
        return (self.question1 + self.question2 + self.question3 + self.question4 + self.question5)

    def save(self, *args, **kwargs):
        self.mark = self.calculate_mark()
        super().save(*args, **kwargs)