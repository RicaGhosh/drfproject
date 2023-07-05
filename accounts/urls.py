from django.urls import path

from .apis import (
    UserDetailRetrieveUpdateDestroy, UserDetailCreate, UserDetailRetrieveOther,
    AddressDetailList ,AddressDetailRetrieveUpdateDestroy, AddressDetailCreate, AddressDetailListOther,
    BankDetailList, BankDetailRetrieveUpdateDestroy, BankDetailCreate, BankDetailListOther,
    EduDetailList, EduDetailRetrieveUpdateDestroy, EduDetailCreate, EduDetailListOther,
    CombinedAllUsersList, CombinedListSelf, CombinedListOther
    ) 


urlpatterns = [

    # ---- USER DETAIL URLS ---- #

    path("userdetail/", UserDetailRetrieveUpdateDestroy.as_view(), name="User Detail"),
    path('userdetail/create/', UserDetailCreate.as_view(), name="User Detail Create"),
    path('userdetail/<int:id>', UserDetailRetrieveOther.as_view(), name = "Other User Detail"),

    # ---- ADDRESS DETAIL URLS ---- #

    path('addressdetail/', AddressDetailList.as_view(), name = "Address List"),
    path("address/<int:pk>", AddressDetailRetrieveUpdateDestroy.as_view(), name="User Detail"),
    path('address/create/', AddressDetailCreate.as_view(), name="User Detail Create"),
    path('addressdetail/<int:id>', AddressDetailListOther.as_view(), name = "Other User Detail"),

    # ---- BANK DETAIL URLS ---- #

    path('bankdetail/', BankDetailList.as_view(), name = "Address List"),
    path("bank/<int:pk>", BankDetailRetrieveUpdateDestroy.as_view(), name="User Detail"),
    path('bank/create/', BankDetailCreate.as_view(), name="User Detail Create"),
    path('bankdetail/<int:id>', BankDetailListOther.as_view(), name = "Other User Detail"),

    # ---- EDU DEATIL URLS ---- #

    path('edudetail/', EduDetailList.as_view(), name = "Address List"),
    path("edu/<int:pk>", EduDetailRetrieveUpdateDestroy.as_view(), name="User Detail"),
    path('edu/create/', EduDetailCreate.as_view(), name="User Detail Create"),
    path('edudetail/<int:id>', EduDetailListOther.as_view(), name = "Other User Detail"),

    # ---- COMBINED DETAIL URLS ---- #

    path('alldetails/', CombinedAllUsersList.as_view(), name = 'all details'),
    path('mydetails/', CombinedListSelf.as_view(), name = 'my details'),
    path('alldetails/<int:id>', CombinedListOther.as_view(), name = 'others details'),
    
]