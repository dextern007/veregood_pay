from django.db import models

# Create your models here.


class Page(models.Model):
    key = models.CharField(max_length=255,unique=True,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    header_links = models.TextField(max_length=2500, blank=True, null=True)
    content = models.TextField(max_length=2500,blank=True,null=True)
    is_active = models.BooleanField(default=False)


class Meta(models.Model):
    page = models.ForeignKey('Page', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    content = models.TextField(max_length=2500,blank=True,null=True)



class Widget(models.Model):
    key = models.CharField(max_length=255,unique=True,blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    content = models.TextField(max_length=2500,blank=True,null=True)
    is_active = models.BooleanField(default=False)






class CascadeStyle(models.Model):
    page = models.ForeignKey('Page', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(max_length=2500, blank=True, null=True)


class JavaScript(models.Model):
    page = models.ForeignKey('Page', on_delete=models.CASCADE, blank=True, null=True)
    content =      models.TextField(max_length=2500,blank=True,null=True)

class Api(models.Model):
    key = models.CharField(max_length=255, unique=True, blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    content =      models.TextField(max_length=2500,blank=True,null=True)


class JsonSerializer(models.Model):
    headers = models.TextField(blank=True,null=True)
    api     = models.ManyToManyField('Api', blank=True,related_name="serializer")
    title   = models.CharField(max_length=255, unique=True, blank=True, null=True)
    key     = models.CharField(max_length=255, unique=True, blank=True, null=True)
    content =      models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return str(self.key)
class CustomFuction(models.Model):
    api = models.ManyToManyField('Api', blank=True, related_name="function")
    headers = models.TextField(blank=True, null=True)
    key     = models.CharField(max_length=255, unique=True, blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    content = models.TextField(max_length=2500,blank=True,null=True)

    def __unicode__(self):
        return self.id
    def __str__(self):
        return str(self.key)



class View(models.Model):
    pass

