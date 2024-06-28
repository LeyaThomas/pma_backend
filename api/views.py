from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from users.serializers import CusUserSerializer, CompanySerializer
from users.models import Cususer, Company
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView

@permission_classes([AllowAny])
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        cususer_data = request.data
        cususer_data['user'] = user.id

        if cususer_data['role'] == 'admin':
            # Create a new Company instance
            company_serializer = CompanySerializer(data={'name': cususer_data['company']})
            if company_serializer.is_valid():
                company = company_serializer.save()
                cususer_data['company'] = company.id
            else:
                return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Use the existing Company instance passed in the request
            try:
                company = Company.objects.get(name=cususer_data['company'])
                cususer_data['company'] = company.id
            except Company.DoesNotExist:
                return Response({'company': 'Company does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        cususer_serializer = CusUserSerializer(data=cususer_data)
        if cususer_serializer.is_valid():
            cususer_serializer.save()
        else:
            return Response(cususer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@permission_classes([AllowAny])
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer