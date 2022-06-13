from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(render(request,'veregood/main_site/screens/home.html'))