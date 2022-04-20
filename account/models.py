from operator import mod
from django.db import models
from setting.models import Crytpo
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_google_auth = models.BooleanField(default=False)
    google_id      = models.TextField(max_length=1500,blank=True,null=True)

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




