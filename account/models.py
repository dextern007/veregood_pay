from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    is_google_auth  = models.BooleanField(default=False)
    google_id       = models.TextField(max_length=1500,blank=True,null=True)
    mobile_number   = models.CharField(max_length=255,blank=True,null=True,unique=True)
    country_code    = models.CharField(max_length=255,blank=True,null=True)
    image           = models.ImageField(upload_to="profile/images", blank=True, null=True)

    # Veregood
    is_vendor       = models.BooleanField(default=False)
    store_setup     = models.BooleanField(default=False)

    # Goode Pay
    kyc_verified    = models.BooleanField(default=False)







