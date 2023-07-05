from rest_framework import status, views, response, exceptions, permissions
from .models import User
from users import serializers as user_serializers
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken
# from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q
from helpers import keys,messages
from rest_framework.views import APIView
from helpers.functions import IsOwnerOrReadOnly, get_tokens, authenticate
from drf_yasg.utils import swagger_auto_schema

# ---- REGISTER API ---- #

class RegisterApi(generics.CreateAPIView):

    authentication_classes = []
    serializer_class = user_serializers.UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            refresh = get_tokens(user)
            res = {
                keys.TOKEN : refresh,
                keys.USER: serializer.data
            }
            return response.Response(res, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---- LOGIN API ---- #

class LoginApi(APIView):

    authentication_classes = []
    
    @swagger_auto_schema(request_body=user_serializers.LoginSerializer)
    def post(self, request):
        email_or_phone = request.data.get(keys.EMAIL_OR_PHONE)
        password = request.data.get(keys.PASSWORD)
        
        if email_or_phone and password:
            user = authenticate(email_or_phone, password)
            print("user",user)
            
            if not user:
                return response.Response({keys.ERROR: messages.INVALID_CREDENTIALS}, status=status.HTTP_400_BAD_REQUEST)
        
            refresh = get_tokens(user)
            
            res = {
                keys.TOKEN : refresh,
                keys.USER : user_serializers.UserSerializer(user).data
            }
            return response.Response(res, status=status.HTTP_200_OK)
        
        return response.Response({keys.ERROR: messages.INVALID_CREDENTIALS}, status=status.HTTP_400_BAD_REQUEST)
        

# ---- USER RETRIEVE API ---- #
  
class UserApi(generics.RetrieveAPIView):

    """ 
    This is used only when user is authenticated 
    """
    # authentication_classes = [JWTAuthentication, ]
    permission_classes=[IsOwnerOrReadOnly]
    serializer_class = user_serializers.UserSerializer
    
    def get(self, request):
        try:
            user = request.user
            serializer = self.get_serializer(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.UNAUTHORIZED}, status=status.HTTP_401_UNAUTHORIZED)


# ---- LOGOUT API ---- #

class LogoutApi(APIView):

    authentication_classes = [JWTAuthentication, ]
    
    def post(self, request, format=None):
       
        try:
            refresh_token = request.data.get(keys.REFRESH_TOKEN)
            token1 = RefreshToken(refresh_token)

            token2 = token1.access_token
            # token2.blacklist()
            OutstandingToken.objects.filter(token = token2).delete()
            token1.blacklist()

            # OutstandingToken.objects.filter(token = refresh_token).delete()
            # access_token = token.access_token
            # OutstandingToken.objects.filter(token = access_token).delete()
            return response.Response({keys.DETAIL: messages.TOKEN_REVOKE_SUCCESS}, status=status.HTTP_200_OK)
        except Exception as ex:
            return response.Response({keys.DETAIL: str(ex)}, status=status.HTTP_400_BAD_REQUEST)
       

# ---- LIST ALL USERS API ---- #

class ListUsers(generics.ListAPIView):
    
    # authentication_classes = [JWTAuthentication, ]
    serializer_class = user_serializers.UserSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        try:
            queryset = User.objects.all()

            search_query = self.request.query_params.get(keys.SEARCH, None)
            if search_query:
                queryset = queryset.filter(
                    Q(first_name__icontains=search_query) |
                    Q(last_name__icontains=search_query) |
                    Q(email__icontains=search_query) |
                    Q(phone_no__icontains=search_query)
                )
            return queryset
        except:
            return response.Response({keys.DETAIL: messages.NO_PERMISSION}, status=status.HTTP_403_FORBIDDEN)
       