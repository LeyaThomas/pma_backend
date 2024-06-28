# views.py
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,viewsets
from rest_framework.generics import RetrieveAPIView , ListAPIView
from .models import Project, ProjectEmployee, EmployeeAnswer
from users.models import Cususer
from .serializers import ProjectEmployeeSerializer, ProjectSerializer, ProjectEmployeeSerializer, CususerSerializer, EmployeeAnswerSerializer, EmployeeMarkSerializer, ProjectStatusSerializer, EmployeeProjectDeadlineSerializer ,ProjectEmployeeDetailSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import get_object_or_404


@permission_classes([AllowAny])
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        project = serializer.save()
        employee_id = self.request.data.get('employeeId')
        ProjectEmployee.objects.create(project=project, employee_id=employee_id)

@permission_classes([AllowAny])
class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer




@permission_classes([AllowAny])
class ProjectEmployeeListCreateView(generics.ListCreateAPIView):
    queryset = ProjectEmployee.objects.all()
    serializer_class = ProjectEmployeeSerializer


@permission_classes([AllowAny])
class EmployeeProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        employee_id = self.kwargs['pk']
        
        return Project.objects.filter(projectemployee__employee_id=employee_id)

@permission_classes([AllowAny])
class ProjectEmployeesView(generics.ListAPIView):
    serializer_class = CususerSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Cususer.objects.filter(projectemployee__project_id=project_id)
    
@permission_classes([AllowAny])
class EmployeeAnswerViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAnswer.objects.all()
    serializer_class = EmployeeAnswerSerializer

@permission_classes([AllowAny])
class EmployeeMarkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeAnswer.objects.all()
    serializer_class = EmployeeMarkSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.query_params.get('project_id', None)
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        return queryset
    
@permission_classes([AllowAny])   
class ProjectCountView(APIView):
    def get(self, request, format=None):
        total_projects = Project.objects.count()
        return Response({'total_projects': total_projects})
    
@permission_classes([AllowAny])   
class UserProjectCountView(APIView):
    def get(self, request, user_id, format=None):
        try:
            cususer = Cususer.objects.get(id=user_id)
        except Cususer.DoesNotExist:
            return Response({'error': 'Cususer with this ID does not exist.'}, status=404)
        
        user_projects_count = ProjectEmployee.objects.filter(employee=cususer).values('project').distinct().count()
        return Response({'user_projects_count': user_projects_count})
    
@permission_classes([AllowAny])    
class ProjectUpdateStatusView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectStatusSerializer

@permission_classes([AllowAny])
class EmployeeProjectDeadlineView(generics.ListAPIView):
    serializer_class = EmployeeProjectDeadlineSerializer

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return ProjectEmployee.objects.filter(employee__id=employee_id, project__deadline__gte=timezone.now()).order_by('project__deadline')

@permission_classes([AllowAny])    
class ProjectEmployeesView(ListAPIView):
    serializer_class = ProjectEmployeeDetailSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return ProjectEmployee.objects.filter(project__id=project_id)
    
@permission_classes([AllowAny])    
class ProjectEmployeeMarksView(ListAPIView):
    serializer_class = EmployeeAnswerSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return EmployeeAnswer.objects.filter(project__id=project_id)
    
