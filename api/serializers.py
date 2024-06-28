from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

@permission_classes([AllowAny])
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Assuming User, CusUser and Company models are related and accessible
        user = self.user
        cususer = user.cususer
        company = cususer.company

        # Add extra responses here
        data['userid'] = user.id
        data['cususerid'] = cususer.id
        data['companyid'] = company.id
        print(data)
        return data