#users.urls.py
from django.urls import path
from .views import CompanyListView, UserDetailView

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='companylist'),
    path('userdetail/<int:pk>/', UserDetailView.as_view(), name='userdetail'),
]