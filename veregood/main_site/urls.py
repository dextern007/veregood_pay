from django.contrib import admin
from django.urls import path,include
from veregood.main_site.site_view import *


app_name = "veregood"

urlpatterns = [


    # API VERSION 1.0 DIWAHAR
    path('', index,name="index"),
    path('home/', index,name="index"),

]
