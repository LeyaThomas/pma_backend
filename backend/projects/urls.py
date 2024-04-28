#projects.urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroyView ,ProjectEmployeeListCreateView, EmployeeProjectsView, ProjectEmployeesView, EmployeeAnswerViewSet, EmployeeMarkViewSet
 
router = DefaultRouter()
router.register('employeeanswer', EmployeeAnswerViewSet)

urlpatterns = [
    path('create/', ProjectListCreateView.as_view(), name='project-create'),
    path('view/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('projectemployee/', ProjectEmployeeListCreateView.as_view()),
    path('employee/<int:pk>/', EmployeeProjectsView.as_view()),
    path('employee-projects/<int:pk>/', EmployeeProjectsView.as_view(), name='employee-projects'),
    path('project/<int:project_id>/employees/', ProjectEmployeesView.as_view()),
    path('', include(router.urls)),
    path('employee-marks/', EmployeeMarkViewSet.as_view({'get': 'list'}), name='employee-marks'),
    
]
    