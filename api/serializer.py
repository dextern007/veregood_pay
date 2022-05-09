from rest_framework import serializers
from account.models import User
from veregood_service.models import *
from rest_framework_gis.serializers import GeometryField,GeoFeatureModelSerializer


class GeometryPointFieldSerializerFields(GeometryField):

    def to_internal_value(self, value):
        try:
            value = value.split(",")
        except:
            raise ValidationError(
                _("Enter the co-ordinates in (latitude,longitude). Ex-12,13")
            )
        try:
            latitude = float(value[0])
        except ValueError:
            raise ValidationError(
                _("Enter the co-ordinates in (latitude,longitude). Ex-12,13")
            )
        try:
            longitude = float(value[1])
        except ValueError:
            raise ValidationError(
                _("Enter the co-ordinates in (latitude,longitude). Ex-12,13")
            )
        value = {
            "type": "Point",
            "coordinates": [longitude, latitude]
        }
        value = json.dumps(value)
        try:
            return GEOSGeometry(value)
        except (ValueError, GEOSException, OGRException, TypeError):
            raise ValidationError(
                _('Invalid format: string or unicode input unrecognized as GeoJSON, WKT EWKT or HEXEWKB.'))

    def to_representation(self, value):
        """ """
        value = super(
            GeometryPointFieldSerializerFields, self).to_representation(value)
        # change to compatible with google map
        data = {
            "type": "Point",
            "coordinates": [
                value['coordinates'][1], value['coordinates'][0]
            ]
        }
        return data


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
