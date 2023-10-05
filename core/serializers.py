from rest_framework import serializers
from django.contrib.auth.models import User
from .models import RevenueSpending

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'], first_name = validated_data['first_name'],last_name = validated_data['last_name'])

        return user

class RevenueSpendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueSpending
        fields = '__all__'