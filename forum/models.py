from django.db import models
from service.models import Service
from django.conf import settings

# Create your models here.
class Forum(models.Model):
    pass

class CreateProject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)

    pass

class RaiseFunds(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    pass

class Donate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    pass
