from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cususer, Company

class CusUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cususer
        fields = ['user', 'name', 'phone_number', 'email', 'address', 'role', 'company']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name']