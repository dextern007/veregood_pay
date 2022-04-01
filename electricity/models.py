from django.db import models
from service.models import Service
# Create your models here.
class Electricity(models.Model):
    service = models.OneToOneField(Service,on_delete=models.CASCADE,blank=True,null=True)


