
from rest_framework import serializers

from veregood.models import *


# Promotion and Branding

class BannerSerilaizer(serializers.ModelSerializer):
    class Meta():
        model = Banner
        fields = "__all__"




class BrandSerilaizer(serializers.ModelSerializer):
    class Meta():
        model = Brand
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    class Meta():
        model = Store
        fields = "__all__"



class AddressSerilaizer(serializers.ModelSerializer):
    class Meta():
        model = Address
        fields = "__all__"

# Cart

class CartItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = CartItem
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer(many=True)
    class Meta():
        model = Cart
        fields = "__all__"











# Product and Product Listing

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model = ProductReview
        exclude = ["user"]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = ProductImage
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = "__all__"


class ListingSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta():
        model = ProductListing
        fields = "__all__"


class CollectionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Collection
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = "__all__"

class CategoryProductSerializer(serializers.ModelSerializer):
    category_product = ProductSerializer(many=True)
    class Meta():
        model = Category
        fields = "__all__"







class VariationSerailizer(serializers.ModelSerializer):
    class Meta():
        model = Variation
        fields = "__all__"

class VariationGroupSerializer(serializers.ModelSerializer):
    varation = VariationSerailizer(many=True,read_only=True)
    class Meta():
        model = VariationGroup
        fields = "__all__"

class ProductDetail(serializers.ModelSerializer):
    category  = CategorySerializer()
    brand     = BrandSerilaizer()
    store    = VendorSerializer()
    variation_group = VariationGroupSerializer(many=True)
    product_image = ProductImageSerializer(many=True)
    class Meta():
        model = Product
        fields = "__all__"



# Order and Payment

class PaymentSerilaizer(serializers.ModelSerializer):
    class Meta():
        model = Payment
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    cart     = CartSerializer()
    payment  = PaymentSerilaizer()
    class Meta():
        model = Order
        fields = "__all__"









# WishList

class WishListItemSerializer(serializers.ModelSerializer):
    product   = ProductSerializer()
    class Meta():
        model = WishlistItem
        fields = "__all__"

class WishListSerializer(serializers.ModelSerializer):
    wishitem = WishListItemSerializer(many=True,read_only=True)
    class Meta():
        model = Wishlist
        fields = "__all__"