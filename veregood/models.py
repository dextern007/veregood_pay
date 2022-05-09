from django.conf import settings
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Product(models.Model):
    pass

class Variation(models.Model):
    pass

class VariationType(models.Model):
    pass

class ColorVariation(models.Model):
    pass





class ProductListing(models.Model):
    pass





class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"   

    def __str__(self):                           
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])




class Cart(models.Model):
    user   = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    total  = models.BigIntegerField(default=0)


class CartItems(models.Model):
    pass




class Address(models.Model):
    pass

class Order(models.Model):
    pass




class Payment(models.Model):
    pass
