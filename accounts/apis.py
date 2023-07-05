from rest_framework import response, status, generics, permissions, exceptions
from .models import UserDetail, AddressDetail, BankDetail, EduDetail
from users.models import User
from .serializers import UserDetailSerializer, AddressDetailSerializer, BankDetailSerializer, EduDetailSerializer, CombinedSerializer
from helpers import keys,messages
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from helpers.functions import IsOwnerOrReadOnly


# ---- USER DETAIL APIS ---- #

class UserDetailCreate(generics.CreateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class UserDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_object(self):
        user_id = self.request.user.id
        queryset = UserDetail.objects.get(user__id=user_id)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', True)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data = request.data, partial=partial)
            serializer.is_valid(raise_exception = True)
            self.perform_update(serializer)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response({keys.ERROR: messages.BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
           
class UserDetailRetrieveOther(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny, ]
    
    def get_object(self):
        id = self.kwargs.get(keys.ID)
        queryset = UserDetail.objects.filter(user__id = id).first()
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)


# ---- ADDRESS DETAIL APIS ---- #
    
class AddressDetailCreate(generics.CreateAPIView):
    serializer_class = AddressDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class AddressDetailList(generics.ListAPIView):
    serializer_class = AddressDetailSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = AddressDetail.objects.filter(user__id=user_id)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset()
            serializer = self.get_serializer(instance, many = True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)

class AddressDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        user_id = self.request.user.id
        pk = self.kwargs.get(keys.PK)
        queryset = AddressDetail.objects.filter(user__id=user_id, id = pk)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', True)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data = request.data, partial=partial)
            serializer.is_valid(raise_exception = True)
            self.perform_update(serializer)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response({keys.ERROR: messages.BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
    
class AddressDetailListOther(generics.ListAPIView):
    serializer_class = AddressDetailSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        id = self.kwargs.get(keys.ID)
        queryset = AddressDetail.objects.filter(user__id = id)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset()
            serializer = self.get_serializer(instance, many = True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
    

# ---- BANK DETAIL APIS ---- #
    
class BankDetailCreate(generics.CreateAPIView):
    serializer_class = BankDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class BankDetailList(generics.ListAPIView):
    serializer_class = BankDetailSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = BankDetail.objects.filter(user__id=user_id)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset()
            serializer = self.get_serializer(instance, many = True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)

class BankDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BankDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        user_id = self.request.user.id
        pk = self.kwargs.get(keys.PK)
        queryset = BankDetail.objects.filter(user__id=user_id, id = pk)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop(keys.PARTIAL, True)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data = request.data, partial=partial)
            serializer.is_valid(raise_exception = True)
            self.perform_update(serializer)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response({keys.ERROR: messages.BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
    
class BankDetailListOther(generics.ListAPIView):
    serializer_class = BankDetailSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        id = self.kwargs.get(keys.ID)
        queryset = BankDetail.objects.filter(user__id = id)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset()
            serializer = self.get_serializer(instance, many = True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
    

# ---- EDU DETAIL APIS ---- #
    
class EduDetailCreate(generics.CreateAPIView):
    serializer_class = EduDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class EduDetailList(generics.ListAPIView):
    serializer_class = EduDetailSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = EduDetail.objects.filter(user__id=user_id)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset()
            serializer = self.get_serializer(instance, many = True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)

class EduDetailRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EduDetailSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        user_id = self.request.user.id
        pk = self.kwargs.get(keys.PK)
        queryset = EduDetail.objects.filter(user__id=user_id, id = pk)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop(keys.PARTIAL, True)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data = request.data, partial=partial)
            serializer.is_valid(raise_exception = True)
            self.perform_update(serializer)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return response.Response({keys.ERROR: messages.BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
    
class EduDetailListOther(generics.ListAPIView):
    serializer_class = EduDetailSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        id = self.kwargs.get(keys.ID)
        queryset = EduDetail.objects.filter(user__id = id)
        return queryset
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_queryset()
            serializer = self.get_serializer(instance, many = True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return response.Response({keys.DETAIL: messages.NO_CONTENT}, status=status.HTTP_204_NO_CONTENT)
    

# ---- COMBINED DETAIL APIS ---- #

"""
 Combined All Details of User
"""

class CombinedAllUsersList(generics.ListAPIView):
    serializer_class = CombinedSerializer
    permission_classes = [IsAdminUser, ]
    queryset = User.objects.all()


class CombinedListSelf(generics.ListAPIView):
    serializer_class = CombinedSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = User.objects.filter(id=user_id)
        return queryset


class CombinedListOther(generics.ListAPIView):
    serializer_class = CombinedSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user_id = self.kwargs.get(keys.ID)
        queryset = User.objects.filter(id=user_id)
        return queryset

       