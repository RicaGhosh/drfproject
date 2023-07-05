from rest_framework import serializers
from .models import User
from helpers import functions, keys, messages
from django.core.validators import RegexValidator

class UserSerializer(serializers.ModelSerializer):
    phone_regex = RegexValidator(
            regex = r'^91[6-9]\d{9}$',
            message= messages.PHONE_REGEX
    )
    
    phone_no = serializers.CharField(validators = [phone_regex])
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'phone_no')
        read_only_fields = ('id',)
        extra_kwargs ={'password': {'write_only': True}}

    def create(self, validated_data):
        instance = functions.create_user(user=validated_data)
        return instance

class LoginSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)