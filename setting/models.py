from django.db import models

# Create your models here.


# List of Payment Gateway with unique titles
class PAYMENTGATEWAY(models.Model):
    title     = models.CharField(max_length=255,unique=True)
    key       = models.TextField(max_length=1500)
    secrect   = models.TextField(max_length=1500)
    web_url   = models.URLField(blank=True,null=True)

    def __str__(self):
        return  self.title

    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Payment Gateway"


class PAYMENTPARTNER(models.Model):
    title     = models.CharField(max_length=255,unique=True)
    key       = models.TextField(max_length=1500)
    secrect   = models.TextField(max_length=1500)
    web_url   = models.URLField(blank=True,null=True)

    def __str__(self):
        return  self.title

    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Payout"


class SMSGATEWAY(models.Model):
    title = models.CharField(max_length=255, unique=True)
    key = models.TextField(max_length=1500)
    secrect = models.TextField(max_length=1500)
    web_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Sms Gateway"

class NOTIFICATION_PROVIDER(models.Model):
    title = models.CharField(max_length=255, unique=True)
    key = models.TextField(max_length=1500)
    secrect = models.TextField(max_length=1500)
    web_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Notification"

class Crytpo(models.Model):
    title          =    models.CharField(max_length=255, unique=True)
    image_url      =    models.ImageField(upload_to="crypto/logo/images",blank=True,null=True)
    wallet_address =    models.TextField(max_length=1500,blank=True,null=True)

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Cryto"


# countries