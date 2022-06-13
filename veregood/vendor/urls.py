
from django.urls import path,include
from veregood.vendor.site_view import *


app_name = 'veregood_vendor'

urlpatterns = [

    # API VERSION 1.0 DEXTER
    path('login/',                     login_vendor ,name="login"),
    path('verify-otp/',                google_otp_verification,name="otp-verification"),  
    path('forgot-password/',           forgot_password_otp_verification,name="forgot-password"),
    path('update-password/',           update_password,name="update-password"),
    path('check-user/',                verify_vendor_availabilty,name="check-user"),
    path('dashboard/',                 dashboard,name="dashboard"),
    path('register/',                  register,name="register"),

]
