from rest_framework import serializers
from account.models import Vendor
from veregood.models import *
from rest_framework_gis.serializers import GeometryField,GeoFeatureModelSerializer



class VendorSerializer(serializers.ModelSerializer):
    class Meta():
        model = Vendor
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Vendor
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta():
        model = Cart
        fields = "__all__"

class WishListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Wishlist
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta():
        model = Order
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = "__all__"