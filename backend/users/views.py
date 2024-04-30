from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics
from .models import Company, Cususer
from .serializers import CompanySerializer, CusUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.http import Http404

# Create your views here.
@permission_classes([AllowAny])
class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

@permission_classes([AllowAny])
class UserDetailView(APIView):
    def get_object(self, pk):
        try:
            return Cususer.objects.get(pk=pk)
        except Cususer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cususer = self.get_object(pk)
        serializer = CusUserSerializer(cususer)
        return Response(serializer.data)