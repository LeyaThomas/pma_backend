# serializers.py
from rest_framework import serializers
from .models import Project, ProjectEmployee, Cususer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectEmployeeSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = ProjectEmployee
        fields = ['project']

class CususerSerializer(serializers.ModelSerializer):
    projects = ProjectEmployeeSerializer(source='projectemployee_set', many=True, read_only=True)
    class Meta:
        model = Cususer
        fields = '__all__'  # replace with the fields you want to include