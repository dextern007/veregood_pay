from django.db import models
from service.models import Service
# Create your models here.


class Finance(models.Model):
    service = models.OneToOneField(Service,on_delete=models.CASCADE,blank=True,null=True)


class Provider(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to="service/finance/provider",blank=True,null=True)
    description = models.TextField(max_length=1500,blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)



