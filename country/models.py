from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True,unique=True)
    code = models.CharField(max_length=255,blank=True,null=True,unique=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class State(models.Model):
    country  = models.ForeignKey(Country,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True,unique=True)
    code = models.CharField(max_length=255,blank=True,null=True,unique=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class City(models.Model):
    state  = models.ForeignKey(State,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True,unique=True)
    code = models.CharField(max_length=255,blank=True,null=True,unique=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
