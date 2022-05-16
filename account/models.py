from django.contrib.gis.db import models
from setting.models import Crytpo
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    is_google_auth = models.BooleanField(default=False)
    google_id      = models.TextField(max_length=1500,blank=True,null=True)
    mobile_number = models.CharField(max_length=255,blank=True,null=True,unique=True)
    country_code  = models.CharField(max_length=255,blank=True,null=True)
    kyc_verified   = models.BooleanField(default=False)
    image = models.ImageField(upload_to="profile/images", blank=True, null=True)


class BANKDETAIL(models.Model):
    user                = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    account_holder_name = models.CharField(max_length=255,blank=True,null=True)
    account_number = models.CharField(max_length=255,blank=True,null=True)
    bank_code = models.CharField(max_length=255,blank=True,null=True)
    verified  = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Bank Details"

class UPI(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    upi_id = models.CharField(max_length=255, blank=True, null=True)
    verified  = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = "UPI"

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile/images",blank=True,null=True)
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    google_id = models.CharField(max_length=255,blank=True,null=True)
    is_google_auth = models.BooleanField(default=False)
    def __unicode__(self):
        return self.id



class CryptoAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    crypto = models.ForeignKey(Crytpo,on_delete=models.CASCADE,blank=True,null=True)
    address = models.TextField(max_length=1500,blank=True,null=True)
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Crypto Address"


class KYC(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    proof_one =models.CharField(max_length=255, blank=True, null=True)
    proof_one_image =models.ImageField(upload_to="proof/one/images",blank=True,null=True)
    proof_two =models.CharField(max_length=255, blank=True, null=True)
    proof_two_image =models.ImageField(upload_to="proof/two/images",blank=True,null=True)
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = "KYC Verification"


class Contact(models.Model):
    user          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name          = models.CharField(max_length=255,blank=True,null=True)
    contact_name  = models.CharField(max_length=255,blank=True,null=True)
    contact_number= models.CharField(max_length=255,blank=True,null=True)
    contact_id    = models.CharField(max_length=255,blank=True,null=True)

    def __unicode__(self):
        return self.id


class DeviceVerification(models.Model):
    mobile_number = models.CharField(max_length=255,blank=True,null=True)
    ip_address = models.CharField(max_length=255,blank=True,null=True)
    otp = models.CharField(max_length=255,blank=True,null=True)



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