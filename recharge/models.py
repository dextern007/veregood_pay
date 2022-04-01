from django.db import models
from service.models import Service
from django.conf import settings

# Create your models here.
class Operator(models.Model):
    title   = models.CharField(max_length=255,blank=True,null=True)
    country = models.CharField(max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class Package(models.Model):
    operator       = models.ForeignKey(Operator, blank=True, null=True,on_delete=models.CASCADE)
    title          = models.CharField(max_length=255,blank=True,null=True)
    description    = models.TextField(max_length=1500,blank=True,null=True)
    package_amount = models.BigIntegerField(default=0)
    duration       = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


PAYMENT_STATUS=(
    ("success","success"),
    ("failure", "failure"),
    ("processing", "processing"),
)

RECHARGE_STATUS=(
    ("success","success"),
    ("failure", "failure"),
    ("processing", "processing"),
)
class Purchase(models.Model):
    service  = models.ForeignKey(Service,on_delete=models.CASCADE,blank=True,null=True)
    user     = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator,blank=True,null=True,on_delete=models.CASCADE)
    package  = models.ForeignKey(Package,blank=True,null=True,on_delete=models.CASCADE)
    subscriber_id = models.CharField(max_length=255,blank=True,null=True)
    mobile_number = models.CharField(max_length=255,blank=True,null=True)
    email = models.CharField(max_length=255,blank=True,null=True)
    payment_amount  = models.BigIntegerField(default=0)
    payment_status  = models.CharField(choices=PAYMENT_STATUS,max_length=255,blank=True,null=True)
    recharge_status  = models.CharField(choices=RECHARGE_STATUS,max_length=255,blank=True,null=True)
    completed        = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
