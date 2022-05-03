from rest_framework import serializers
from account.models import User
from veregood_service.models import *

#  Good Epay
class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = "__all__"


# Veregood

class VereGoodServiceListing(serializers.ModelSerializer):
    class Meta():
        model = VendorService
        fields = "__all__"


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
        
class VendorServiceSerializer(serializers.ModelSerializer):
    review= ReviewSerializer(many=True)
    portfolio= PortfolioSerializer(many=True)
    class Meta():
        model = VendorService
        fields = "__all__"