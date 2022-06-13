from rest_framework import serializers
from account.models import User
from veregood_service.models import Vendor
from veregood_service.models import *
from rest_framework_gis.serializers import GeometryField,GeoFeatureModelSerializer


#  Auth
class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = "__all__"










# Veregood Service

class VereGoodServiceListing(serializers.ModelSerializer):
    class Meta():
        model = VendorService
        fields = "__all__"
        depth = 1

class ReviewSerializer(serializers.ModelSerializer):
    class Meta():
        model = Review
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = "__all__"
        depth = 2

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta():
        model = Portfolio
        fields = "__all__"
        
class VendorServiceSerializer(GeoFeatureModelSerializer):
    review= ReviewSerializer(many=True)
    portfolio= PortfolioSerializer(many=True)
    #location = GeometryPointFieldSerializerFields(source='location.location')
    class Meta():
        model = VendorService
        fields = "__all__"
        depth = 1
        geo_field = "location"

