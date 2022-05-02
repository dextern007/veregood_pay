from django.contrib import admin
from django.urls import path
from api.views import *




urlpatterns = [
    # API VERSION 1.0 DIWAHAR
    path('verify-mobile/', VerifyMobile.as_view()),
    path('auth/', AuthView.as_view()),
    path('vendors/', VendorServiceView.as_view()),
    path('booking/', BookingView.as_view()),
    path('rating/', RatingView.as_view()),

]
