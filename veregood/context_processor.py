
from veregood.models import Category

def main_category(request):
    categories = Category.objects.filter(parent=None)
    return {'categories': categories}