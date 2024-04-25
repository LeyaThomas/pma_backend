from django.shortcuts import render
from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

# Create your views here.
@permission_classes([AllowAny])
class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer