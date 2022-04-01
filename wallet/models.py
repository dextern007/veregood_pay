from django.db import models
from django.conf import  settings
from setting.models import Crytpo
import  uuid
# Create your models here.
class Wallet(models.Model):
    user      =      models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    wallet_id =      models.UUIDField(default=uuid.uuid4(),unique=True)
    balance   =      models.BigIntegerField(blank=True,null=True)
    base_currency = models.CharField(default="USD",max_length=100)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)



    def __unicode__(self):
        return self.id



class CryptoWallet(models.Model):
    wallet         =      models.ForeignKey(Wallet,on_delete=models.CASCADE,blank=True,null=True)
    crypto         =      models.ForeignKey(Crytpo,on_delete=models.CASCADE,blank=True,null=True)
    balance        =      models.BigIntegerField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.id



TRANSACTION_CHOICES = (
    ('transfer','transfer'),
    ('request','request'),
    ('recieved','recieved'),
    ('deposit', 'deposit'),
    ('withdraw', 'withdraw'),
)
STATUS_CHOICES = (
    ('submited','submited'),
    ('on_process','on_process'),
    ('success','success'),
    ('failure', 'failure'),
)

class CryptoTransaction(models.Model):
    crypto_wallet = models.ForeignKey(CryptoWallet,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=255, blank=True, null=True)
    transaction_amount = models.BigIntegerField(blank=True, null=True)
    transaction_type = models.CharField(choices=TRANSACTION_CHOICES, max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.id



class Transaction(models.Model):
    wallet    =      models.OneToOneField(Wallet,on_delete=models.CASCADE,blank=True,null=True)
    title     =      models.CharField(max_length=255,blank=True,null=True)
    status    =      models.CharField(choices=STATUS_CHOICES,max_length=255,blank=True,null=True)
    transaction_amount = models.BigIntegerField(blank=True,null=True)
    transaction_type = models.CharField(choices=TRANSACTION_CHOICES,max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.wallet.id


