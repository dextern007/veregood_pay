from django.contrib import admin
from account.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class MyUserAdmin(UserAdmin):
    model = User
    list_display = ["username","email","first_name","last_name","is_staff","is_vendor",]
    list_filter = ["is_staff","is_vendor",]
    labels = {
            "username":"Mobile Number"
         }


admin.site.register(User,MyUserAdmin)