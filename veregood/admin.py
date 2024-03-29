from attr import field
from django.contrib import admin
from veregood.models import *
# Register your models here.
from django.contrib.admin import AdminSite
import nested_admin
from account.models import User
from django.contrib.auth.admin import UserAdmin

class VendorAdminSite(AdminSite):
    site_header = "VereGood | Seller Portal"
    site_title  = "VereGood | Seller Portal"
    index_title = "VereGood | Seller Portal"

vendor_admin_site = VendorAdminSite(name='vendor_admin')


class VariationInline(nested_admin.NestedStackedInline):
    model = Variation
    extra = 0


class VariationGroupInline(nested_admin.NestedTabularInline):
    model = VariationGroup
    inlines = [VariationInline]
    extra = 0
  
    
class ImageInline(nested_admin.NestedTabularInline):
    model = ProductImage
    extra = 0

class ColorInline(nested_admin.NestedTabularInline):
    model = ColorVariation
    extra = 0

class WeighInline(nested_admin.NestedTabularInline):
    model = WeightVariation
    extra = 0

class LengthInline(nested_admin.NestedTabularInline):
    model = LengthVariation
    extra = 0

class PackageInline(nested_admin.NestedTabularInline):
    model = PackagingVariation
    extra = 0

class DescriptionInline(admin.StackedInline):
    model = ProductDescription

class GuideInline(admin.StackedInline):
    model = ProductGuide

class MetaInline(admin.StackedInline):
    model = ProductMeta

class TabInline(admin.StackedInline):
    model = ProductTab
    extra = 0

class ProductAdmin(nested_admin.NestedModelAdmin):
    inlines       = [DescriptionInline,GuideInline,VariationInline,ColorInline,WeighInline,LengthInline,PackageInline,ImageInline,MetaInline,TabInline]
    list_display  = ["sku","title","short_description","in_stock","is_approved"]
    list_filter   = ["is_approved"]
    search_fields = ["sku"]
    fields = ["image","thumbnail","product_type","title",	"sku", "short_description","brand","category", "price","quantity","in_stock","has_variation","has_weight","has_color","has_length","has_package","page_layout",]

    class Meta:
        model = Product


class ProductListingInline(admin.TabularInline):
    model = ProductListing
    extra = 0     

class CollectionAdmin(nested_admin.NestedModelAdmin):
    inlines       = [ProductListingInline]


    class Meta:
        model = Collection




from django.urls import reverse
from django.shortcuts import redirect
class VendorProductAdmin(nested_admin.NestedModelAdmin):
    inlines       = [DescriptionInline,TabInline,VariationInline,ColorInline,WeighInline,LengthInline,PackageInline,ImageInline,MetaInline]
    list_display  = ["sku","title","short_description","in_stock","is_approved"]
    list_filter   = ["is_approved"]
    search_fields = ["sku"]
    fields        = ["image","thumbnail","product_type","title","sku", "short_description","brand", "price","quantity","in_stock","has_variation","has_weight","has_color","has_length","has_package","page_layout"]
    view_on_site = False
    class Meta:
        model = Product


    # Demo Site
    def view_on_site(self, obj):
        return 'https://example.com'

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/veregood/vendor/dashboard')

    def response_change(self, request, obj):
        return redirect('/veregood/vendor/dashboard/product/?filter=unapproved')    







vendor_admin_site.register(Store)
vendor_admin_site.register(Product,VendorProductAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Address)
admin.site.register(Store)
admin.site.register(Brand)
admin.site.register(ProductReview)
admin.site.register(ProductImage)
admin.site.register(Variation)
admin.site.register(Collection,CollectionAdmin)
admin.site.register(ProductListing)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(Banner)
admin.site.register(Order)
admin.site.register(Payment)