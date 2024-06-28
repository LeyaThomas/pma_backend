#users.urls.py
from django.urls import path
from .views import CompanyListView, UserDetailView, UserCountView

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='companylist'),
    path('userdetail/<int:pk>/', UserDetailView.as_view(), name='userdetail'),
    path('usercount/', UserCountView.as_view(), name='usercount'),
]