from django.shortcuts import render
from pages.models import Page
# Create your views here.


def page_view(request,page_key):
    page=Page.objects.get(page_key=page_key)
    return render(request,'pages/page.html',{'page':page})