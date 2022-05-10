import uuid
from django.conf import settings
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class Brand(models.Model):
    title  =  models.CharField(max_length=255,blank=True,null=True)
    is_active =  models.BooleanField(default=False)

PRODUCT_TYPE = (
    ("simple","simple"),
    ("variable","variable"),
    ("acution","acution"),
    ("quote","quote"),
)


class Product(models.Model):
    title             =  models.CharField(max_length=255,blank=True,null=True)
    category          =  models.ForeignKey('Category',blank=True,null=True,on_delete=models.CASCADE)
    brand             =  models.ForeignKey('Brand',blank=True,null=True,on_delete=models.CASCADE)
    image             =  models.ImageField(upload_to="veregood/product/image/",blank=True,null=True)
    thumbnail         =  models.ImageField(upload_to="veregood/product/image/thumnail/",blank=True,null=True)
    description       =  models.TextField(max_length=5500,blank=True,null=True)
    short_description =  models.TextField(max_length=5500,blank=True,null=True)
    price             =  models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    rating            =  models.DecimalField(decimal_places=1,max_digits=3,default=0.0)
    has_color         =  models.BooleanField(default=False)
    has_weight        =  models.BooleanField(default=False)
    product_type      =  models.CharField(choices=PRODUCT_TYPE,default="simple",max_length=255)
    is_active         =  models.BooleanField(default=False)


class ProductReview(models.Model):
    product           =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_review",blank=True,null=True)
    user              =  models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    rating            =  models.DecimalField(decimal_places=1,max_digits=3,default=0.0)
    description       =  models.TextField(max_length=1500,blank=True,null=True)



class ProductImage(models.Model):
    product           =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image",blank=True,null=True)
    image             =  models.ImageField(upload_to="veregood/product/image/",blank=True,null=True)
    is_active         =  models.BooleanField(default=False)





class Variation(models.Model):
    pass

class VariationType(models.Model):
    pass

class ColorVariation(models.Model):
    pass





class ProductListing(models.Model):
    pass





class Category(MPTTModel):
    is_active =  models.BooleanField(default=False)
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
    payment_id  = models.CharField(uuid.uuid4,primary_key=True,unique=True,max_length=255)
    status      = models.CharField(max_length=255)

# we_1KxuqWHx0vNusgVBUqGAEUXm
# pk_test_51HRl3PHx0vNusgVB3hNqHisqtao9aquG13JrIs2NLaLOg2RvJSqjAwk6fbp1H3OFm7FRWsCWN1QjiN4i63TZAJTX00Fqftv4j2
# sk_test_51HRl3PHx0vNusgVBAUxH7TOXeDy0lYT6UzJRzMXQvfEm3KaHSFTyjNFCzxoUyYsjHbPQAtNQKbm6B4vsSz0wCsgh00UjXo7Cwj