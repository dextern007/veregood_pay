from django.db import models
import uuid


# Create your models here.
class Payment(models.Model):
    payment_id = models.CharField(max_length=255,unique=True,default=uuid.uuid4())
    reference_id = models.CharField(max_length=255,blank=True,null=True)
    payment_method = models.CharField(max_length=255,blank=True,null=True)
    amount = models.BigIntegerField(default=0)
    status = models.CharField(max_length=255,blank=True,null=True)
    status_code = models.CharField(max_length=255,blank=True,null=True)
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.payment_id

    def __unicode__(self):
        return self.id