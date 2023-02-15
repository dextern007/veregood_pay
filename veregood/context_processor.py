
from veregood.models import Category,WebSiteLogs
from django.urls import resolve


def main_category(request):
    categories = Category.objects.filter(parent=None)


    return {'categories': categories}