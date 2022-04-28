from pyexpat import model
from attr import fields
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
        
