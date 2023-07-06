from django.urls import path
from .apis import RegisterApi, LoginApi, UserApi, LogoutApi, ListUsers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', RegisterApi.as_view(), name = "register"),
    path('login/', LoginApi.as_view(), name = "login"),
    
    # path('login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path('login/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    path("me/", UserApi.as_view(), name = "me"),
    path("userlist/", ListUsers.as_view(), name = "users"),
    path("logout/", LogoutApi.as_view(), name= "logout"),
]