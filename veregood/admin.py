from django.contrib import admin
from veregood.models import *
# Register your models here.

admin.site.register(Address)
admin.site.register(Store)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(ProductImage)
admin.site.register(Variation)
admin.site.register(VariationGroup)
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

