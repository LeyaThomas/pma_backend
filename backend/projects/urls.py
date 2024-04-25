#projects.urls.py
from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroyView ,ProjectEmployeeListCreateView, EmployeeProjectsView, ProjectEmployeesView
 


urlpatterns = [
    path('create/', ProjectListCreateView.as_view(), name='project-create'),
    path('view/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('projectemployee/', ProjectEmployeeListCreateView.as_view()),
    path('employee/<int:pk>/', EmployeeProjectsView.as_view()),
    path('employee-projects/<int:pk>/', EmployeeProjectsView.as_view(), name='employee-projects'),
    path('project/<int:project_id>/employees/', ProjectEmployeesView.as_view()),
    
]
    