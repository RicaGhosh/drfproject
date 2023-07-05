from rest_framework import serializers
from .models import UserDetail, AddressDetail, BankDetail, EduDetail
from users.serializers import UserSerializer
from datetime import date
from django.core.validators import RegexValidator
from helpers import keys, messages
from users import models as user_models


# ---- USER DETAIL SERIALIZER ---- #

class UserDetailSerializer(serializers.ModelSerializer):
    def validate_dob(self, date):
        age = (date.today() - date).days // 365

        if age < 18:
            raise serializers.ValidationError(messages.VALID_AGE)
        return date

    # dob = serializers.DateField(validators=[validate_birthdate])

    class Meta:
        model = UserDetail
        fields = '__all__'
        read_only_fields = ('user',)


# ---- ADDRESS DETAIL SERIALIZER ---- #

class AddressDetailSerializer(serializers.ModelSerializer):
    
    def validate_pincode(self, value):
        digits_len = 6
        if len(str(value)) != digits_len:
            raise serializers.ValidationError(messages.VALID_PINCODE)
        return value
    
    # pincode = serializers.IntegerField(validators = [validate_pincode, ])
    
    class Meta:
        model = AddressDetail
        fields = '__all__'
        read_only_fields = ('user',)


# ---- BANK DETAIL SERIALIZER ---- #

class BankDetailSerializer(serializers.ModelSerializer):
    
    def validate_account_no(self, value):
        digits_len = 16
        if len(str(value)) != digits_len:
            raise serializers.ValidationError(messages.VALID_ACC_NO)
        return value
        
    ifsc_regex = RegexValidator(
        regex = r'^[A-Z]{4}0[A-Z0-9]{6}$',
        message= messages.VALID_IFSC)
        
    # account_no = serializers.IntegerField(validators = [validate_acc_no])
    ifsc_code = serializers.CharField(validators = [ifsc_regex])
    
    class Meta:
        model = BankDetail
        fields = '__all__'
        read_only_fields = ('user',)


# ---- EDU DETAIL SERIALIZER ---- #

class EduDetailSerializer(serializers.ModelSerializer):

    def validate_marks(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError(messages.VALID_MARKS)
        return value       

   # marks = serializers.FloatField(validators = [validate_marks])
    class Meta:
        model = EduDetail
        fields = '__all__'
        read_only_fields = ('user',)


# ---- COMBINED SERIALIZER ---- #

class CombinedSerializer(serializers.ModelSerializer):
    # user = UserSerializer(source='*')
    user_details = serializers.SerializerMethodField(read_only=True)
    address_details = serializers.SerializerMethodField(read_only=True)
    bank_details = serializers.SerializerMethodField(read_only=True)
    edu_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = user_models.User
        fields ='__all__'
    
    def get_user_details(self,instance):
        if UserDetail.objects.filter(user=instance).exists():
            instance = UserDetail.objects.get(user=instance)
            return UserDetailSerializer(instance).data
        return {}
    
    def get_address_details(self,instance):
        if AddressDetail.objects.filter(user=instance).exists():
            instance = AddressDetail.objects.filter(user=instance)
            return AddressDetailSerializer(instance,many=True).data
        return []
    
    def get_bank_details(self,instance):
        if BankDetail.objects.filter(user=instance).exists():
            instance = BankDetail.objects.filter(user=instance)
            return BankDetailSerializer(instance,many=True).data
        return []
    
    def get_edu_details(self, instance):
        if EduDetail.objects.filter(user= instance).exists():
            instance = EduDetail.objects.filter(user= instance)
            return EduDetailSerializer(instance, many= True).data
        return []
