from django.contrib.gis.db import models
from tinymce.models import HTMLField
# Create your models here.
class Page(models.Model):
    title    = models.CharField(max_length=255,blank=True,null=True)
    page_key = models.CharField(max_length=255,blank=True,null=True,unique=True)
    body  = HTMLField()
    content = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.page_key


class Meta(models.Model):
    page  = models.OneToOneField(Page,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    keyword = models.TextField(max_length=5500,blank=True,null=True)
    description = models.TextField(max_length=5500,blank=True,null=True)