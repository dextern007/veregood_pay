from django.db import models
from service.models import Service
from django.conf import settings

# Create your models here.
class Job(models.Model):
    service = models.OneToOneField(Service,on_delete=models.CASCADE,blank=True,null=True)

class Company(models.Model):
    logo = models.ImageField(upload_to="service/jobs/companies/",blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    describtion = models.TextField(max_length=1500,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

class Category(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    describtion = models.TextField(max_length=1500,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

JOB_TYPE= (
    ("part_time","part_time"),
    ("full_time", "full_time"),
)
class Post(models.Model):
    job         = models.ForeignKey(Job,on_delete=models.CASCADE,blank=True,null=True)
    job_title   = models.CharField(max_length=255,blank=True,null=True)
    job_type    = models.CharField(choices=JOB_TYPE,max_length=255,blank=True,null=True)
    country     = models.CharField(max_length=255,blank=True,null=True)
    describtion = models.TextField(max_length=5000,blank=True,null=True)
    category    = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    company     = models.ForeignKey(Company,on_delete=models.CASCADE,blank=True,null=True)
    experience  = models.CharField(max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

class Resume(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    file = models.FileField(upload_to="service/jobs/resumes/",blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

STATUS =(
    ("shortlisted","shortlisted"),
    ("rejected","rejected"),
    ("submitted","submitted"),
)

class Application(models.Model):
    user  = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True)
    resume = models.ForeignKey(Resume,on_delete=models.CASCADE,blank=True,null=True)
    status = models.CharField(choices=STATUS,max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)