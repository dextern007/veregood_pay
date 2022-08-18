from django.contrib import admin
from django.urls import path,include
from veregood.payment.views import *

app_name ="payment"


urlpatterns = [


    # URLS VERSION 1.0 DEXTER
    path('create_checkout_session/<int:id>', create_checkout_session , name="checkout_session"),
    path('sucess',  PaymentSuccessView.as_view() , name="success"),
    path('failure', PaymentFailedView.as_view() , name="failure"),

   

]
