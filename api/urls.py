from django.contrib import admin
from django.urls import path,include
from api.views import *




urlpatterns = [
    # API VERSION 1.0 DIWAHAR
    path('vendors/', VendorServiceView.as_view()),
    path('booking/', BookingView.as_view()),
    path('rating/', RatingView.as_view()),
    path('register-vendor/', CreateVendor.as_view()),
    path('veregood/', include('veregood.urls')),

]
