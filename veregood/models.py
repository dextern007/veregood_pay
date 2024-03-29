
import random
import uuid
from django.conf import settings
from django.contrib.gis.db import models
from mptt.models import MPTTModel, TreeForeignKey
from tinymce.models import HTMLField
from country.models import Country,State,City
from currency.models import Currency
# from taggit.managers import TaggableManager

# Create your models here.
DELIVERY_TYPE =(
    ('self','self'),
    ('veregood','veregood'),
)


# Vendor
class Store(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    vendor_id               = models.CharField(default=uuid.uuid4,unique=True,max_length=255)
    logo                    = models.ImageField(upload_to="logo/",blank=True,null=True)
    store_name              = models.CharField(max_length=255,blank=True,null=True)
    store_describtion       = models.CharField(max_length=255,blank=True,null=True)
    contact_mobile_number   = models.CharField(max_length=255,blank=True,null=True)
    contact_email           = models.CharField(max_length=255,blank=True,null=True)
    address                 = models.TextField(max_length=1000,blank=True,null=True)
    state                   = models.CharField(max_length=100,blank=True,null=True)
    city                    = models.CharField(max_length=100,blank=True,null=True)
    country                 = models.CharField(max_length=100,blank=True,null=True)
    location                = models.PointField(null=True,blank=True,srid=4326,verbose_name='Location')
    location_name           = models.CharField(max_length=100,blank=True,null=True)
    gst_number              = models.CharField(max_length=100,blank=True,null=True)
    upi_id                  = models.CharField(max_length=100,blank=True,null=True)
    rating                  = models.DecimalField(default=0.0,max_digits=10,decimal_places=1)
    delivery_type           = models.CharField(max_length=100,choices=DELIVERY_TYPE,default="self")
    available_regions       = models.ManyToManyField(Country,blank=True)
    base_currency           = models.ForeignKey(Currency,on_delete=models.CASCADE,blank=True,null=True)

    # others
    commision_percentage    = models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
    profile_picture         = models.ImageField(upload_to="profile/",blank=True,null=True)
    dob                     = models.DateField(blank=True,null=True)
    age                     = models.IntegerField(default=18)
    aadhar_number           = models.CharField(max_length=100,blank=True,null=True)
    pan_number              = models.CharField(max_length=100,blank=True,null=True)
    closed                  = models.BooleanField(default=False)
    
    is_active               = models.BooleanField(default=False)
    store_setup             = models.BooleanField(default=False)
    is_approved             = models.BooleanField(default=False)
    kyc_verified            = models.BooleanField(default=False)
    payment_method_added    = models.BooleanField(default=False)




class STOREBANKACCOUNT(models.Model):
    account_name            = models.CharField(max_length=255,blank=True,null=True)
    account_number	        = models.CharField(max_length=255,blank=True,null=True)
    bank_name	            = models.CharField(max_length=255,blank=True,null=True)
    bank_address	        = models.CharField(max_length=255,blank=True,null=True)
    routing_number	        = models.CharField(max_length=255,blank=True,null=True)
    iban	                = models.CharField(max_length=255,blank=True,null=True)
    swift_code              = models.CharField(max_length=255,blank=True,null=True)
    ifsc_code               = models.CharField(max_length=255,blank=True,null=True)


class STOREKYC(models.Model):
    vendor_name             = models.CharField(max_length=255,blank=True,null=True)
    vendor_proof_number     = models.CharField(max_length=255,blank=True,null=True)
    vendor_proof            = models.ImageField(upload_to="profile/",blank=True,null=True)




class Banner(models.Model):
    # product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image",blank=True,null=True)
    image                   =  models.ImageField(upload_to="veregood/banner/image/",blank=True,null=True)
    is_active               =  models.BooleanField(default=False)
    mobile                  =  models.BooleanField(default=False)
    web                     =  models.BooleanField(default=False)

    
class Address(models.Model):
    user                    = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True,related_name="useraddress")
    first_name              =  models.CharField(max_length=255,blank=True,null=True)
    last_name               =  models.CharField(max_length=255,blank=True,null=True)
    emai_address            =  models.CharField(max_length=255,blank=True,null=True)
    flat_no                 = models.CharField(max_length=100,blank=True,null=True)
    address                 =  models.TextField(max_length=1500,blank=True,null=True)
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


LAYOUT = (
    ("layout_1","Layout 1"),
    ("layout_2","Layout 2"),
    ("layout_3","Layout 3"),
    ("layout_4","Layout 4"),
    ("layout_5","Layout 5 - Supports 3D Sliders"),

)

CURRENCY = (
    ("INR","INR"),
    ("USD","USD"),
    ("EUR","EUR"),
)

class Product(models.Model):
    store                   =  models.ForeignKey(Store,on_delete=models.CASCADE,blank=True,null=True)
    title                   =  models.TextField(max_length=1500,blank=True,null=True)
    sku                     =  models.CharField(max_length=255,blank=True,null=True,unique=True)
    # main_category           =  models.ForeignKey('MainCategory',blank=True,null=True,on_delete=models.CASCADE,related_name="main_category_product")
    category                =  models.ForeignKey('Category',blank=True,null=True,on_delete=models.CASCADE,related_name="category_product")
    brand                   =  models.ForeignKey('Brand',blank=True,null=True,on_delete=models.CASCADE)
    image                   =  models.ImageField(upload_to="veregood/product/image/",blank=True,null=True)
    thumbnail               =  models.ImageField(upload_to="veregood/product/image/thumnail/",blank=True,null=True)
    short_description       =  models.TextField(max_length=5500,blank=True,null=True)
    currency                =  models.CharField(default="USD",choices=CURRENCY,max_length=10)
    price                   =  models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    rating                  =  models.DecimalField(decimal_places=1,max_digits=3,default=0.0)
    has_color               =  models.BooleanField(default=False)
    has_length              =  models.BooleanField(default=False)
    has_weight              =  models.BooleanField(default=False)
    has_package             =  models.BooleanField(default=False)
    has_variation           =  models.BooleanField(default=False)
    product_type            =  models.CharField(choices=PRODUCT_TYPE,default="simple",max_length=255)
    is_active               =  models.BooleanField(default=False)
    in_stock                =  models.BooleanField(default=False)
    quantity                =  models.BigIntegerField(default=0)
    page_layout             =  models.CharField(choices=LAYOUT,default="layout_1",max_length=100)
    is_approved             =  models.BooleanField(default=False)
    draft                   =  models.BooleanField(default=True)
    start_date              =  models.DateField(blank=True,null=True)
    end_date                =  models.DateField(blank=True,null=True)


class ColorVariation(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="color",blank=True,null=True)
    color_code              =  models.CharField(max_length=255,blank=True,null=True)
    active                  =  models.BooleanField(default=False)

class WeightVariation(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="weight",blank=True,null=True)
    weight                  =  models.CharField(max_length=255,blank=True,null=True)
    measurement             =  models.CharField(max_length=255,blank=True,null=True)
    active                  =  models.BooleanField(default=False)
 

class LengthVariation(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="length",blank=True,null=True)
    length                  =  models.CharField(max_length=255,blank=True,null=True)
    measurement             =  models.CharField(max_length=255,blank=True,null=True)
    active                  =  models.BooleanField(default=False)
 

class PackagingVariation(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="package",blank=True,null=True)
    package                 =  models.CharField(max_length=255,blank=True,null=True)
    measurement             =  models.CharField(max_length=255,blank=True,null=True)
    active                  =  models.BooleanField(default=False)
 

class ProductReview(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_review",blank=True,null=True)
    user                    =  models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    rating                  =  models.DecimalField(decimal_places=1,max_digits=3,default=0.0)
    description             =  models.TextField(max_length=1500,blank=True,null=True)

    class Meta:
        # Add verbose name
        verbose_name = 'Review'

class ProductImage(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product_image",blank=True,null=True)
    image                   =  models.ImageField(upload_to="veregood/product/image/",blank=True,null=True)
    is_active               =  models.BooleanField(default=False)

    class Meta:
        # Add verbose name
        verbose_name = 'Image'

class ProductDescription(models.Model):
    product                 =  models.OneToOneField(Product,on_delete=models.CASCADE,blank=True,null=True,related_name="description")
    content                 =  HTMLField()

    class Meta:
        # Add verbose name
        verbose_name = 'Description'

class ProductGuide(models.Model):
    product                 =  models.OneToOneField(Product,on_delete=models.CASCADE,blank=True,null=True)
    content                 =  HTMLField()

    class Meta:
        # Add verbose name
        verbose_name = 'Guide'


class ProductTab(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True,related_name="product_tab")
    title                   =  models.CharField(max_length=255,blank=True,null=True)
    content                 =  models.TextField(max_length=5000,blank=True,null=True)

    class Meta:
        # Add verbose name
        verbose_name = 'Tab'

class ProductMeta(models.Model):
    product                 =  models.OneToOneField(Product,on_delete=models.CASCADE,blank=True,null=True)
    title                   = models.CharField(max_length=255,blank=True,null=True)
    keyword                 = models.TextField(max_length=5500,blank=True,null=True)
    description             = models.TextField(max_length=5500,blank=True,null=True)

    class Meta:
        # Add verbose name
        verbose_name = 'Meta'

class ProductQuote(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True,related_name="product_quote")
    user                    =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    content                 =  models.TextField()

class ProductBid(models.Model):
    product                 =  models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True,related_name="product_bid")
    user                    =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    bid_amount              =  models.BigIntegerField(default=0)


VARIATION_TITLE = (
    ('color','color'),
    ('size','size'),
    ('weight','weight'),
    ('packaging','packaging'),
)

class VariationGroup(models.Model):
    product                 =  models.ForeignKey('Product',on_delete = models.CASCADE,blank=True,null=True,related_name="varation_group")
    has_price               =  models.BooleanField(default=False)
    title                   =  models.CharField(choices=VARIATION_TITLE,default="simple",max_length=100)
    suffix                  =  models.CharField(max_length=100,blank=True,null=True)

    class Meta:
        # Add verbose name
        verbose_name = 'Variation Group'

class Variation(models.Model):
    product                 =  models.ForeignKey('Product',on_delete = models.CASCADE,blank=True,null=True,related_name="variation")
    variation_group         =  models.ForeignKey('VariationGroup',on_delete = models.CASCADE,blank=True,null=True,related_name="group_varation")
    image                   =  models.ImageField(upload_to="veregood/product/variation/image/",blank=True,null=True)
    thumbnail               =  models.ImageField(upload_to="veregood/product/image/variation/thumnail/",blank=True,null=True)
    title                   =  models.CharField(max_length=255,blank=True,null=True)
    price                   =  models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
    is_active               =  models.BooleanField(default=False)
    in_stock                =  models.BooleanField(default=False)
    quantity                =  models.BigIntegerField(default=0)

    class Meta:
        # Add verbose name
        verbose_name = 'Variation'

class CollectionGroup(models.Model):
    image                   =  models.ImageField(upload_to="veregood/collection/group/icon",blank=True,null=True)
    title                   =  models.CharField(max_length=255,blank=True,null=True)
    active                  =  models.BooleanField(default=False)

class Collection(models.Model):
    collection_group        =  models.ForeignKey(CollectionGroup,on_delete=models.CASCADE,blank=True,null=True,related_name="collections")
    title                   =  models.CharField(max_length=255,blank=True,null=True)
    slug                    =  models.CharField(max_length=255,blank=True,null=True,unique=True)
    icon                    =  models.ImageField(upload_to="veregood/collection/icon",blank=True,null=True)
    image                   =  models.ImageField(upload_to="veregood/collection/image",blank=True,null=True)
    is_active               =  models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProductListing(models.Model):
    collection              = models.ForeignKey(Collection,on_delete=models.CASCADE,blank=True,null=True,related_name="product_listing")
    product                 = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    

#######






#######


class Category(MPTTModel):
    icon                    =  models.ImageField(upload_to="veregood/sub_category/icon",blank=True,null=True)
    image                   =  models.ImageField(upload_to="veregood/sub_category/image",blank=True,null=True)
    is_active               =  models.BooleanField(default=False)              
    name                    =  models.CharField(max_length=200)
    slug                    =  models.SlugField(unique=True)
    parent                  =  TreeForeignKey(
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

ATTRIBUTE_TYPE =(
    ("text","text"),
    ("table","table"),
    ("input","input"),
    ("popup","popup"),
    ("link","link"),
    ("dropdown_selection","dropdown_selection"),
)

class Attribute(models.Model):
    title             =  models.CharField(max_length=255,blank=True,null=True)
    category          =  models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True,related_name="attributes")
    attribute_type    =  models.CharField(max_length=255,default=ATTRIBUTE_TYPE)
    sortable          =  models.IntegerField(default=0)
    is_active         =  models.BooleanField(default=False)



class Cart(models.Model):
    user                    = models.OneToOneField(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    total                   = models.BigIntegerField(default=0)
    sub_total                   = models.BigIntegerField(default=0)


class CartItem(models.Model):
    cart                    = models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,null=True,related_name="cart_item")
    product                 = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    variation               = models.ManyToManyField(Variation,blank=True)
    has_variation           = models.BooleanField(default=False)
    quantity                = models.IntegerField(default=0)
    line_total              = models.IntegerField(default=0)

#######
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
    ('picked','picked'),
    ('pending','pending'),
    ('abonded','abonded'),
    ('delivered','delivered'),
    ('recieved ','recieved'),
    ('on_the_way','on_the_way'),
    ('recived_by_delivery','recived_by_delivery'),
    ('delayed','delayed'),

)

PAYMENT_TYPE=(
    ("online","online"),
    ("cod","cod"),
)

class Order(models.Model):
    payment             = models.ForeignKey("Payment",on_delete=models.CASCADE,blank=True,null=True)
    user                = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    # payment_id          = models.CharField(max_length=255,blank=True,null=True,unique=True)
    cart                = models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,null=True)
    location            = models.PointField(null=True,blank=True,srid=4326,verbose_name='Location')
    total               = models.BigIntegerField(default=0)
    coupoun_discount    = models.BigIntegerField(default=0)
    delivery_charge     = models.BigIntegerField(default=0)
    tax                 = models.BigIntegerField(default=0)
    final_total         = models.BigIntegerField(default=0)
    status              = models.CharField(choices=PROCESS,max_length=100,default="onprocess")
    payment_type        = models.CharField(choices=PAYMENT_TYPE,max_length=100,default="onprocess")
    coupun_applied      = models.BooleanField(default=False)
    address             = models.TextField(max_length=1500,blank=True,null=True)
    billing_address             = models.TextField(max_length=1500,blank=True,null=True)
    shipping_address             = models.TextField(max_length=1500,blank=True,null=True)
    customer_otp        = models.CharField(default=str(random.randint(1000,9999)),max_length=255)
    delivery_status_notes = models.CharField(max_length=255,blank=True,null=True)
    vendor_status_notes = models.CharField(max_length=255,blank=True,null=True)
    cancelled           = models.BooleanField(default=False)
    cancelled_reason    = models.CharField(max_length=255,blank=True,null=True)


class VendorOrder(models.Model):
    vendor              = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    order               = models.ForeignKey(Order,on_delete=models.CASCADE,blank=True,null=True)
    product             = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    cancelled           = models.BooleanField(default=False)
    cancelled_reason    = models.CharField(max_length=255,blank=True,null=True)

class Quote(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    contact_mobile = models.CharField(max_length=255,blank=True,null=True)
    contact_email  = models.CharField(max_length=255,blank=True,null=True)

class Auction(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    bid_amount = models.BigIntegerField(default=0)



class Payment(models.Model):
    payment_id          = models.CharField(default=uuid.uuid4,primary_key=True,unique=True,max_length=255)
    payment_reference_id          = models.CharField(blank=True,null=True,max_length=255)
    status              = models.CharField(max_length=255)
    amount_paid         = models.IntegerField(default=0)
    amount              = models.IntegerField(default=0)
    paid                = models.BooleanField(default=False)
    captured            = models.BooleanField(default=False)




class Explore(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
    title   = models.CharField(max_length=255)
    video   = models.FileField(upload_to="veregood/explore/videos",blank=True,null=True)
    image   = models.ImageField(upload_to="veregood/explore/images",blank=True,null=True)
    active  = models.BooleanField(default=False)


class WebSiteLogs(models.Model):
    # user  = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=models.CASCADE)
    count   = models.IntegerField(default=0)
    date    = models.DateField(blank=True,null=True,unique=True)
    current_url = models.CharField(max_length=255,blank=True,null=True)