from django.db import models
from service.models import Service
from django.conf import settings
# Create your models here.



class DTH(models.Model):
    service = models.OneToOneField(Service,on_delete=models.CASCADE,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

