# serializers.py
from rest_framework import serializers
from .models import Project, ProjectEmployee, Cususer, EmployeeAnswer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectEmployeeSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)
    project_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = ProjectEmployee
        fields = ['employee_id', 'project_id', 'project']

    def create(self, validated_data):
        employee_id = validated_data.pop('employee_id')
        project_id = validated_data.pop('project_id')

        employee = Cususer.objects.get(id=employee_id)
        project = Project.objects.get(id=project_id)

        return ProjectEmployee.objects.create(employee=employee, project=project, **validated_data)

class CususerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cususer
        
        fields = '__all__'  

class ProjectEmployeeDetailSerializer(serializers.ModelSerializer):
    employee = CususerSerializer(read_only=True)

    class Meta:
        model = ProjectEmployee
        fields = ['employee']

class EmployeeAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAnswer
        fields = ['id', 'project', 'employee', 'mark', 'question1', 'question2', 'question3', 'question4', 'question5']
        read_only_fields = ['mark']

class EmployeeMarkSerializer(serializers.ModelSerializer):
    employee = serializers.StringRelatedField()  # This will include the employee's string representation

    class Meta:
        model = EmployeeAnswer
        fields = ['employee', 'mark']

class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['status']

class ProjectDeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'status', 'deadline']

class EmployeeProjectDeadlineSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = ProjectEmployee
        fields = ['project']


