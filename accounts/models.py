from django.db import models
from django.conf import settings

# Create your models here.

# ---- USER DETAIL MODEL ---- #

class UserDetail(models.Model):

    class GenderChoices(models.TextChoices):
        MALE = "MALE"
        FEMALE = "FEMALE"
        TRANSGENDER = 'TRANSGENDER'
        PREFER_NOT_TO_SAY = "PREFER NOT TO SAY"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_details", verbose_name='user')
    gender = models.CharField(max_length=255, choices=GenderChoices.choices, default=GenderChoices.PREFER_NOT_TO_SAY, verbose_name="Gender")
    dob = models.DateField(verbose_name="dob") 
    father_name = models.CharField(max_length=255, verbose_name="Father's Name")
    mother_name = models.CharField(max_length=255, verbose_name="Mother's Name")

    def __str__(self):
        return str(self.user)


# ---- ADDRESS DETAIL MODEL ---- #

class AddressDetail(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="address_details", verbose_name='user')
    area = models.CharField(max_length=255, verbose_name="Area")
    city = models.CharField(max_length=255, verbose_name="City")  # 3rd P API - Choices
    state = models.CharField(max_length=255, verbose_name="State")  # 3rd P API - Choices
    country = models.CharField(max_length=255, verbose_name="Country")  # 3rd P API - Choices
    pincode = models.IntegerField(verbose_name="Pincode")


# ---- BANK DETAIL MODEL ---- #

class BankDetail(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bank_details", verbose_name='user')
    bankname = models.CharField(max_length=255, verbose_name="Bank Name")  # 3rd P API - Choices
    account_no = models.IntegerField(verbose_name="Account Number")  # VALIDATIONS 
    ifsc_code = models.CharField(max_length=11, verbose_name="IFSC Code")  # VALIDATIONS 

    
# ---- EDU DETAIL MODEL ---- #

class EduDetail(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="edu_details", verbose_name='user')
    institute = models.CharField(max_length=255, verbose_name="Institute Name")  # 3rd P API - Choices
    uni_board = models.CharField(max_length=255, verbose_name="University / Board")  # 3rd P API - Choices
    course = models.CharField(max_length=255, verbose_name="Course")  # 3rd P API - Choices
    pass_year = models.DateField(verbose_name="Passing Year")  
    marks = models.FloatField(verbose_name="Aggregate Marks (%)") 
