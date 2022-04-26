from django.contrib import admin
from veregood_service.models import *
from mapwidgets.widgets import GooglePointFieldWidget

class ImageInline(admin.TabularInline):
    model = Portfolio
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class VendorServiceAdmin(admin.ModelAdmin):
    
    inlines = [ImageInline,ReviewInline]
    model = VendorService
    formfield_overrides = {
                            models.PointField: {"widget": GooglePointFieldWidget}
                          }

# Register your models here.
# admin.site.register(WorldBorder)
admin.site.register(VereGoodService)
admin.site.register(Vendor)
admin.site.register(Booking)
admin.site.register(VendorService,VendorServiceAdmin)
