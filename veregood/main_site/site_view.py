from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(render(request,'main_site/screens/home.html'))

def login(request):
    return HttpResponse(render(request,'main_site/screens/login.html'))

def signup(request):
    return HttpResponse(render(request,'main_site/screens/register.html'))

def cart(request):
    return HttpResponse(render(request,'main_site/screens/cart.html'))