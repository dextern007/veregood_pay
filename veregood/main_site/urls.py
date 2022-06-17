from django.contrib import admin
from django.urls import path,include
from veregood.main_site.site_view import *
from pages.views import page_view


app_name = "veregood"

urlpatterns = [


    # API VERSION 1.0 DIWAHAR
    path('', index,name="index"),
    path('home/', index,name="index"),
    path('login/',login,name="login"),
    path('register/',signup,name="register"),
    path('cart/',cart,name="cart"),
    path('page/<str:page_key>/',page_view,name="page"),
]
