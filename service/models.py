from django.db import models

# Create your models here.
class Category(models.Model):
    title     = models.CharField(max_length=255,blank=True,null=True)
    slug      = models.CharField(max_length=255,unique=True,blank=True)
    image_url = models.ImageField(upload_to="images/category",blank=True,null=True)


    def __str__(self):
        return  self.slug

class Service(models.Model):
    category  = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    title     = models.CharField(max_length=255,blank=True,null=True)
    slug      = models.CharField(max_length=255,unique=True,blank=True)
    image_url = models.ImageField(upload_to="images/service",blank=True,null=True)


    def __str__(self):
        return  self.slug


