from pyexpat import model
from django.contrib import admin
from pages.models import Page,Meta
# Register your models here.
class MetaInline(admin.StackedInline):
    model = Meta


class PageAdmin(admin.ModelAdmin):
    inlines = [MetaInline]
    class Meta:
        model = Page
        fields ="__all__"

admin.site.register(Page,PageAdmin)