from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from helpers import keys, messages

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name: str, last_name: str, email: str, password: str = None, is_staff=False, is_superuser= False) -> "User":
        if not email:
            raise ValueError(messages.VALUE_ERROR_EMAIL)
        if not first_name:
            raise ValueError(messages.VALUE_ERROR_FNAME)
        if not last_name:
            raise ValueError(messages.VALUE_ERROR_LNAME)
        
        user = self.model(email= self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
    
    def create_superuser(self, first_name:str, last_name: str, email: str, password: str) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()
        return user


class User(AbstractUser):
   
    first_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    phone_no = models.CharField(max_length=12) 

    objects = UserManager()

    USERNAME_FIELD = "email"  # or mobile - regex
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.first_name+" "+self.last_name
