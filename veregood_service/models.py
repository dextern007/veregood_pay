from django.contrib.gis.db import models
from django.conf import settings
import uuid

# Create your models here.


class Vendor(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    vendor_id               = models.CharField(default=uuid.uuid4,unique=True,max_length=255)
    address                 = models.TextField(max_length=1000,blank=True,null=True)
    state                   = models.CharField(max_length=100,blank=True,null=True)
    city                    = models.CharField(max_length=100,blank=True,null=True)
    location                = models.PointField(null=True,blank=True,srid=4326,verbose_name='Location')
    location_name           = models.CharField(max_length=100,blank=True,null=True)
    gst_number              = models.CharField(max_length=100,blank=True,null=True)
    upi_id                  = models.CharField(max_length=100,blank=True,null=True)
    rating                  = models.DecimalField(default=0.0,max_digits=10,decimal_places=1)
    commision_percentage    = models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
    profile_picture         = models.ImageField(upload_to="profile/",blank=True,null=True)
    logo                    = models.ImageField(upload_to="logo/",blank=True,null=True)
    dob                     = models.DateField(blank=True,null=True)
    age                     = models.IntegerField(default=18)
    aadhar_number           = models.CharField(max_length=100,blank=True,null=True)
    pan_number              = models.CharField(max_length=100,blank=True,null=True)
    store_name              = models.CharField(max_length=255,blank=True,null=True)
    store_describtion       = models.CharField(max_length=255,blank=True,null=True)
    contact_mobile_number   = models.CharField(max_length=255,blank=True,null=True)
    contact_email           = models.CharField(max_length=255,blank=True,null=True)
    closed                  = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=False)


class VereGoodService(models.Model):
    service_name  = models.CharField(max_length=255,blank=True,null=True,unique=True)
    service_image = models.ImageField(upload_to="veregood_service/images",blank=True,null=True)
    service_icon = models.ImageField(upload_to="veregood_service/icon",blank=True,null=True)

    def __str__(self):
        return self.service_name

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




