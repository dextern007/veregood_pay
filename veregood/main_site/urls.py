from django.contrib import admin
from django.urls import path,include
from veregood.main_site.site_view import *
from pages.views import page_view


app_name = "veregood"

urlpatterns = [
    # API VERSION 1.0 ( Nora Spensers ) URL ROUTING & Template Designing
    path('', index,name="index"),
    path('home/',index,name="home"),
    path('login/',main_login,name="login"),
    path('register/',signup,name="register"),
    path('otp-verification/',verification,name="otp-verification"),
    path('cart/',cart,name="shopping-cart"),
    path('dashboard/',dashboard,name="my-account"),
    path('category/',category,name="product-listing"),
    path('product/<int:pk>/',product,name="product"),
    path('page/<str:page_key>/',page_view,name="page"),
    path('checkout/',checkout,name="checkout"),
    path('wishlist/',wishlist,name="wishlist"),
    path('services/',services,name="services"),
]
