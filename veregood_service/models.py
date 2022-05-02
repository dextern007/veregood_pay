
from statistics import mode
from django.contrib.gis.db import models

# Create your models here.

class VereGoodService(models.Model):
    service_name  = models.CharField(max_length=255,blank=True,null=True,unique=True)
    service_image = models.ImageField(upload_to="veregood_service/images",blank=True,null=True)
    service_icon = models.ImageField(upload_to="veregood_service/icon",blank=True,null=True)

    def __str__(self):
        return self.service_name



class Vendor(models.Model):
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name  = models.CharField(max_length=255,blank=True,null=True)
    nick_name  = models.CharField(max_length=255,blank=True,null=True)
    email      = models.CharField(max_length=255,blank=True,null=True)
    mobile_number      = models.CharField(max_length=255,blank=True,null=True)
    rating     = models.IntegerField(default=0)


    def __str__(self):
        return self.nick_name



class VendorService(models.Model):
    vendor            =   models.ForeignKey(Vendor,blank=True,null=True,on_delete=models.CASCADE)
    service_type      =   models.ForeignKey(VereGoodService,blank=True,null=True,on_delete=models.CASCADE)
    name              =   models.CharField(max_length=255,blank=True,null=True)
    description       =   models.TextField(max_length=2500,blank=True,null=True)
    profile_image     =   models.ImageField(upload_to="vendor/profile/images/",blank=True,null=True)
    location          =   models.PointField(blank=True,null=True)
    available         =   models.BooleanField(default=False)
    rating            =   models.IntegerField(default=0)
    charge            =   models.DecimalField(max_digits=10,decimal_places=2,default=0.00)


class Review(models.Model):
    user              =   models.CharField(max_length=255,blank=True,null=True)
    vendor_service    =   models.ForeignKey(VendorService,blank=True,null=True,on_delete=models.CASCADE,related_name="review")
    stars             =   models.IntegerField(default=0)
    description       =   models.TextField(max_length=2500,blank=True,null=True)

class Portfolio(models.Model):
    vendor_service    =   models.ForeignKey(VendorService,blank=True,null=True,on_delete=models.CASCADE,related_name="portfolio")
    image             =   models.ImageField(upload_to="vendor/service/images/",blank=True,null=True)


class Booking(models.Model):
    service           =  models.ForeignKey(VendorService,blank=True,null=True,on_delete=models.CASCADE)
    payment_id        =  models.CharField(max_length=255,blank=True,null=True)
    user_id           =  models.CharField(max_length=255,blank=True,null=True)
    payment_completed =  models.BooleanField(default=False)
    total_amount      =  models.CharField(max_length=255,blank=True,null=True)
    from_date         =  models.DateTimeField(blank=True,null=True)
    to_date           =  models.DateTimeField(blank=True,null=True)




class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name