from django.db import models
from django.conf import settings

class Currency(models.Model):
    title         = models.CharField(max_length=255,blank=True,null=True)
    currency_code = models.CharField(max_length=255,blank=True,unique=True)
    current_price = models.CharField(max_length=255,blank=True,null=True)

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)


class TUSDBALANCE(models.Model):
    wallet = models.OneToOneField(Wallet,blank=True,null=True,on_delete=models.CASCADE)
    balance =  models.CharField(max_length=255,blank=True,null=True)

