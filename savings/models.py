from django.db import models
from service.models import Service
from  django.conf import settings
# Create your models here.
class Saving(models.Model):
    service = models.OneToOneField(Service,on_delete=models.CASCADE,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

class SavingsAccount(models.Model):
    saving        = models.ForeignKey(Saving,on_delete=models.CASCADE,blank=True,null=True)
    user          = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    total_balance = models.BigIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

STATUS =(
    ("breaked","breaked"),
    ("initiated", "initiated"),
    ("processing", "processing"),
    ("completed", "completed"),
)

class Goal(models.Model):
    savings_account = models.ForeignKey(SavingsAccount,on_delete=models.CASCADE,blank=True,null=True)
    goal_title      = models.CharField(blank=True,null=True,max_length=255)
    goal_amount     = models.BigIntegerField(default=0)
    breakage_charges= models.IntegerField(default=0)
    breaked         = models.BooleanField(default=False)
    status          = models.CharField(choices=STATUS,blank=True,null=True,max_length=255)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


TRANSACTION_CHOICES = (
    ('transfer','transfer'),
    ('request','request'),
    ('recieved','recieved'),
    ('deposit', 'deposit'),
    ('withdraw', 'withdraw'),
)
STATUS_CHOICES = (
    ('submited','submited'),
    ('on_process','on_process'),
    ('success','success'),
    ('failure', 'failure'),
)
class GoalTransaction(models.Model):
    goal = models.ForeignKey(Goal,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=255, blank=True, null=True)
    transaction_amount = models.BigIntegerField(blank=True, null=True)
    transaction_type = models.CharField(choices=TRANSACTION_CHOICES, max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.id