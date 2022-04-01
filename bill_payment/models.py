from django.db import models
from recharge.models import Operator
from django.conf import settings
# Create your models here.
BILL_TYPE =(
    ('electricity','electricity'),
    ('water','water'),
    ('postpaid','postpaid'),
    ('others','others')
)

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

class Bill(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    bill_number = models.CharField(blank=True,null=True,max_length=255)
    operator    = models.ForeignKey(Operator,on_delete=models.CASCADE,blank=True,null=True)
    bill_type   = models.CharField(choices=BILL_TYPE,blank=True,null=True,max_length=255)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    payment_amount = models.BigIntegerField(default=0)
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=255, blank=True, null=True)
    recharge_status = models.CharField(choices=RECHARGE_STATUS, max_length=255, blank=True, null=True)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
