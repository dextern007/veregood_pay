
from veregood.models import Category,WebSiteLogs
from django.urls import resolve

from datetime import datetime
now=datetime.now()

def main_category(request):
    categories = Category.objects.filter(parent=None)
    current_url = resolve(request.path_info).url_name
    try:
        logs = WebSiteLogs.objects.get(date=datetime(now.year, now.month, now.day))
        logs.count=logs.count+1
        logs.save()
    except:
        WebSiteLogs.objects.create(
            count=1,
            current_url = current_url
        )

    return {'categories': categories}