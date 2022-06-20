from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(render(request,'main_site/screens/home.html'))

def login(request):
    return HttpResponse(render(request,'main_site/screens/login.html'))

def signup(request):
    return HttpResponse(render(request,'main_site/screens/register.html'))

def verification(request):
    return HttpResponse(render(request,'main_site/screens/otp-verification.html'))

def cart(request):
    return HttpResponse(render(request,'main_site/screens/cart.html'))

def dashboard(request):
    return HttpResponse(render(request,'main_site/screens/dashboard.html'))

def category(request):
    return HttpResponse(render(request,'main_site/screens/category.html'))