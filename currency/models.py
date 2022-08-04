from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True,unique=True)
    code = models.CharField(max_length=255,blank=True,null=True,unique=True)
    symbol = models.CharField(max_length=255,blank=True,null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    from_currency = models.CharField(max_length=255,blank=True,null=True)
    to_currency  = models.CharField(max_length=255,blank=True,null=True)
    exchange_rate = models.CharField(max_length=255,blank=True,null=True)
    active = models.BooleanField(default=False)