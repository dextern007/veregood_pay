import random

import uuid
from django.conf import settings
from django.contrib.gis.db import models

from mptt.models import MPTTModel, TreeForeignKey
from account.models import *

# Create your models here.

class Banner(models.Model):
    # product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image",blank=True,null=True)
    image                   =  models.ImageField(upload_to="veregood/banner/image/",blank=True,null=True)
    is_active               =  models.BooleanField(default=False)

    
class Address(models.Model):
    user                    = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True,related_name="useraddress")
    flat_no                 = models.CharField(max_length=100,blank=True,null=True)
    address                 =  models.CharField(max_length=255,blank=True,null=True)
    city                    = models.CharField(max_length=100,blank=True,null=True)
    state                   = models.CharField(max_length=100,blank=True,null=True)
    country                 = models.CharField(max_length=100,blank=True,null=True)
    location                = models.PointField(null=True,blank=True,srid=4326,verbose_name='Location')


#########

class Brand(models.Model):
    icon                    =  models.ImageField(upload_to="veregood/brands/icon",blank=True,null=True)
    image                   =  models.ImageField(upload_to="veregood/brands/image",blank=True,null=True)
    title                   =  models.CharField(max_length=255,blank=True,null=True)
    is_active               =  models.BooleanField(default=False)



PRODUCT_TYPE = (
    ("simple","simple"),
    ("variable","variable"),
    ("acution","acution"),
    ("quote","quote"),
)


class Product(models.Model):
    vendor                  =  models.ForeignKey(Vendor,on_delete=models.CASCADE,blank=True,null=True)
    title                   =  models.CharField(max_length=255,blank=True,null=True)
    category                =  models.ForeignKey('Category',blank=True,null=True,on_delete=models.CASCADE)
    brand                   =  models.ForeignKey('Brand',blank=True,null=True,on_delete=models.CASCADE)
    image                   =  models.ImageField(upload_to="veregood/product/image/",blank=True,null=True)
    thumbnail               =  models.ImageField(upload_to="veregood/product/image/thumnail/",blank=True,null=True)
    description             =  models.TextField(max_length=5500,blank=True,null=True)
    short_description       =  models.TextField(max_length=5500,blank=True,null=True)
    price                   =  models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    rating                  =  models.DecimalField(decimal_places=1,max_digits=3,default=0.0)
    has_color               =  models.BooleanField(default=False)
    has_variation           =  models.BooleanField(default=False)
    product_type            =  models.CharField(choices=PRODUCT_TYPE,default="simple",max_length=255)
    is_active               =  models.BooleanField(default=False)


class ProductReview(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_review",blank=True,null=True)
    user                    =  models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    rating                  =  models.DecimalField(decimal_places=1,max_digits=3,default=0.0)
    description             =  models.TextField(max_length=1500,blank=True,null=True)



class ProductImage(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image",blank=True,null=True)
    image                   =  models.ImageField(upload_to="veregood/product/image/",blank=True,null=True)
    is_active               =  models.BooleanField(default=False)

class Variation(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True,related_name="variation")
    variation_type          =  models.ForeignKey('VariationType',on_delete=models.CASCADE,blank=True,null=True)
    text                    =  models.CharField(max_length=255,blank=True,null=True)
    value                   =  models.CharField(max_length=255,blank=True,null=True)
    sub_text                =  models.CharField(max_length=255,blank=True,null=True)
    has_price               =  models.BooleanField(default=False)
    addon_price             =  models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    is_active               =  models.BooleanField(default=False)


class VariationType(models.Model):
    title                   =  models.CharField(max_length=255,blank=True,null=True,unique=True)
    is_active               =  models.BooleanField(default=False)


#####



#####

class Collection(models.Model):
    title                   =  models.CharField(max_length=255,blank=True,null=True,unique=True)
    icon                    =  models.ImageField(upload_to="veregood/brands/icon",blank=True,null=True)
    image                   =  models.ImageField(upload_to="veregood/brands/image",blank=True,null=True)
    is_active               =  models.BooleanField(default=False)


class ProductListing(models.Model):
    collection              = models.ForeignKey(Collection,on_delete=models.CASCADE,blank=True,null=True,related_name="product_listing")
    product                 = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)

#######







#######
class Category(MPTTModel):
    icon                    =  models.ImageField(upload_to="veregood/brands/icon",blank=True,null=True)
    image                   =  models.ImageField(upload_to="veregood/brands/image",blank=True,null=True)
    is_active               =  models.BooleanField(default=False)
    name                    = models.CharField(max_length=200)
    slug                    = models.SlugField(unique=True)
    parent                  = TreeForeignKey(
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


########



#########

class Cart(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    total                   = models.BigIntegerField(default=0)


class CartItems(models.Model):
    cart                    = models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,null=True,related_name="cartitem")
    product                 = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    variation               = models.ForeignKey(Variation,on_delete=models.CASCADE,blank=True,null=True)
    quantity                = models.IntegerField(default=0)
    line_total              = models.IntegerField(default=0)

#######


######


class Wishlist(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    timestamp               = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated                 = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.id

class WishlistItem(models.Model):
    wishlist                = models.ForeignKey(Wishlist,related_name='wishitem',on_delete=models.CASCADE,blank=True,null=True)
    product                 = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)

    def __unicode__(self):
        return self.id

######




PROCESS = (
    ('onprocess','onprocess'),
    ('accepted','accepted'),
    # ('preparing','preparing'),
    # ('ready_to_pickup','ready_to_pickup'),
    ('picked','picked'),
    ('pending','pending'),
    ('abonded','abonded'),
    ('delivered','delivered'),
    ('recieved ','recieved'),
    ('on_the_way','on_the_way'),
    # ('preparing','preparing'),
    ('recived_by_delivery','recived_by_delivery'),
    ('delayed','delayed'),

)

PAYMENT_TYPE=(
    ("online","online"),
    ("cod","cod"),
)

class Order(models.Model):
    user                = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    payment_id          = models.CharField(max_length=255,blank=True,null=True,unique=True)
    cart                = models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,null=True)
    location            = models.PointField(null=True,blank=True,srid=4326,verbose_name='Location')
    total               = models.IntegerField(default=0)
    coupoun_discount    = models.IntegerField(default=0)
    delivery_charge     = models.IntegerField(default=0)
    final_total         = models.IntegerField(default=0)
    status              = models.CharField(choices=PROCESS,max_length=100,default="onprocess")
    payment_type        = models.CharField(choices=PAYMENT_TYPE,max_length=100,default="onprocess")
    coupun_applied      = models.BooleanField(default=False)
    address             = models.TextField(max_length=100,blank=True,null=True)
    # vendor_otp          = models.CharField(default=str(random.randint(1000,9999)),max_length=255)
    customer_otp        = models.CharField(default=str(random.randint(1000,9999)),max_length=255)
    delivery_status_notes = models.CharField(max_length=255,blank=True,null=True)




class Payment(models.Model):
    payment_id          = models.CharField(default=uuid.uuid4,primary_key=True,unique=True,max_length=255)
    status              = models.CharField(max_length=255)
    amount_paid         = models.IntegerField(default=0)
    paid                = models.BooleanField(default=False)
    captured            = models.BooleanField(default=False)

# 
# pk_test_51HRl3PHx0vNusgVB3hNqHisqtao9aquG13JrIs2NLaLOg2RvJSqjAwk6fbp1H3OFm7FRWsCWN1QjiN4i63TZAJTX00Fqftv4j2
# 