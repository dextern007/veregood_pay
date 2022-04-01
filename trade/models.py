from django.db import models
from service.models import Service
# Create your models here.

class Currency(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)

class Trade(models.Model):
    service = models.OneToOneField(Service,on_delete=models.CASCADE,blank=True,null=True)

TRADE_TYPE =(
    ('buy','buy'),
    ('sell','sell'),
)

class X(models.Model):
    trade_type = models.CharField(choices=TRADE_TYPE,max_length=255,blank=True,null=True)