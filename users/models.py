from django.db import models
from django.contrib.auth.models import User

# model for company
class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# model for custom user
class Cususer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)  # New role field

    def __str__(self):
        return self.name