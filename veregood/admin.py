from django.contrib import admin
from veregood.models import *
# Register your models here.
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe



class VariationInline(admin.StackedInline):
    model = Variation
    extra = 1

class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
        
    

class ProductAdmin(admin.ModelAdmin):
    inlines       = [VariationInline,ImageInline]
    list_display  = ["sku","title","short_description","in_stock","is_approved"]
    list_filter   = ["is_approved"]
    search_fields = ["sku"]
    class Meta:
        model = Product





admin.site.register(Product,ProductAdmin)


admin.site.register(Address)
admin.site.register(Store)
admin.site.register(Brand)

admin.site.register(ProductReview)
admin.site.register(ProductImage)
admin.site.register(Variation)
admin.site.register(Collection)
admin.site.register(ProductListing)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(Banner)
admin.site.register(Order)
admin.site.register(Payment)

