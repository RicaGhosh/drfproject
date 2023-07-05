from users.models import User
import datetime
import jwt
from django.conf import settings
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from . import keys, messages
from django.db.models import Q

# ---- CREATE USER FUNCTION ---- #

"""
Used in Register Api Endpoint
to create a new user.
"""

def create_user(user) -> "User":
    instance = User(
        first_name = user['first_name'],
        last_name = user['last_name'],
        email = user['email'],
        phone_no = user['phone_no']
    )
    if user['password'] is not None:
        instance.set_password(user['password'])

    instance.save()
    return instance
    

# TOKEN CREATION FUNCTION ---- #

def get_tokens(user):
    refresh = RefreshToken.for_user(user)

    return {
        keys.REFRESH : str(refresh),
        keys.ACCESS: str(refresh.access_token),
    }


# ---- AUTHENTICATE USER ---- #

"""
Used in Login Api Endpoint
to authenticate a user
"""

def authenticate(email_or_phone, password):
    user = User.objects.filter(Q(email = email_or_phone) | Q(phone_no = email_or_phone)).first()
    if user and user.check_password(password):
        return user
    return None


# ---- OWNER PERMISSION FUNCTION ---- #

"""
Used by CRUD Api Endpoints
to allow only the user to perform CRUD operations on their data
"""

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user.id == request.user.id
    