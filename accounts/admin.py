from django.contrib import admin
from .models import UserDetail, AddressDetail, BankDetail, EduDetail

# Register your models here.
class UserDetailAdmin(admin.ModelAdmin):
    list_display =(
        "id",
        "user",
        "gender",
        "dob",
    )

class AddressDetailAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "user",
        "area",
        "city",
        "state",
        "country",
        "pincode"
    )

class BankDetailAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "user",
        "bankname",
        "account_no",
        "ifsc_code"
    )

class EduDetailAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "user",
        "institute",
        "uni_board",
        "course",
        "pass_year",
        "marks"
    )


admin.site.register(UserDetail, UserDetailAdmin)
admin.site.register(AddressDetail, AddressDetailAdmin)
admin.site.register(BankDetail, BankDetailAdmin)
admin.site.register(EduDetail, EduDetailAdmin)
