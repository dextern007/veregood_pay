from django.db import models
from django.conf import settings
from setting.models import Crytpo
# Create your models here.

# Reward Model
class Scratch(models.Model):
    crypto = models.ForeignKey(Crytpo, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    sub_text = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="coupoun/images", blank=True, null=True)
    url = models.TextField(max_length=1500, blank=True, null=True)
    reward_points = models.BigIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.id


REWARD_TYPE=(
    ("coupoun","coupoun"),
    ("scratch", "scratch"),
)
class Reward(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    scratch     = models.ForeignKey(Scratch,blank=True,null=True,on_delete=models.CASCADE)
    coupoun     = models.ForeignKey('Coupoun',blank=True,null=True,on_delete=models.CASCADE)
    reward_type = models.CharField(max_length=255,choices=REWARD_TYPE,blank=True,null=True)
    reedemed    = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.id



# Coupon Model

class Coupoun(models.Model):
    title    = models.CharField(max_length=255,blank=True,null=True)
    text     = models.CharField(max_length=255,blank=True,null=True)
    sub_text = models.CharField(max_length=255,blank=True,null=True)
    image    = models.ImageField(upload_to="coupoun/images",blank=True,null=True)
    url      = models.TextField(max_length=1500,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.id


# Referal Model

class Referal(models.Model):
    user            = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    referal_code    = models.CharField(max_length=255,blank=True,null=True,unique=True)
    referal_points  = models.IntegerField(default=0)
    redeemed_points = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.id

class ReferalNetwork(models.Model):
    referal = models.ForeignKey(Referal,on_delete=models.CASCADE,blank=True,null=True)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.id


# Miner

class Miner(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    valid_hashes    = models.BigIntegerField(default=0)
    invalid_hashes  = models.BigIntegerField(default=0)
    reward_points   = models.BigIntegerField(default=0)
    redeemed_points = models.BigIntegerField(default=0)
    hash_speed      = models.BigIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __unicode__(self):
        return self.id