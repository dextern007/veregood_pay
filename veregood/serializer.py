
from pickletools import read_long1
from pyexpat import model
from numpy import product
from rest_framework import serializers
from account.models import User

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












# Product and Product Listing
class UserReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ["first_name","image"]

class ProductReviewSerializer(serializers.ModelSerializer):
    # user = UserReviewSerializer()
    class Meta():
        model = ProductReview
        exclude =["user"]
        
class ProductReviewListSerializer(serializers.ModelSerializer):
    user = UserReviewSerializer()
    class Meta():
        model = ProductReview
        fields = "__all__"

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

class VariationGroupSerailizer(serializers.ModelSerializer):
    group_variation = VariationSerailizer(many=True)
    class Meta():
        model = VariationGroup
        fields = "__all__"


class ProductDetail(serializers.ModelSerializer):
    
    category  = CategorySerializer()
    brand     = BrandSerilaizer()
    store    = VendorSerializer()
    varation_group = VariationGroupSerailizer(many=True)
    product_image = ProductImageSerializer(many=True)
    
    class Meta():
        model = Product
        fields = "__all__"










# Cart

class CartItemSerializer(serializers.ModelSerializer):
    product =ProductSerializer()
    variation = VariationSerailizer(many=True)
    class Meta():
        model = CartItem
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer(many=True)
    class Meta():
        model = Cart
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

# Order and Payment

class PaymentSerilaizer(serializers.ModelSerializer):
    class Meta():
        model = Payment
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    item     = CartItemSerializer()
    payment  = PaymentSerilaizer()
    class Meta():
        model = Order
        fields = "__all__"


class QuoteSerializer(serializers.ModelSerializer):
    user = UserReviewSerializer()
    class Meta():
        model = Quote
        fields = "__all__"


class AuctionSerializer(serializers.ModelSerializer):
    user = UserReviewSerializer()
    class Meta():
        model = Auction
        fields = "__all__"


class ExploreSerializer(serializers.ModelSerializer):
    class Meta():
        model = Explore
        fields = "__all__"


class CollectionInline(serializers.ModelSerializer):
    class Meta():
        model = Collection
        fields = "__all__"

class CollectionGroupSerializer(serializers.ModelSerializer):
    collections = CollectionInline(many=True)
    class Meta():
        model = CollectionGroup
        fields = "__all__"