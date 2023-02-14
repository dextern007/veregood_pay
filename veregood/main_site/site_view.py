import email
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from account.models import User
from veregood.models import *
from veregood.vendor.forms import VendorProfileEditForm, VendorProfileForm
from django.views.generic.edit import *



def index(request):
    try:
        new_products = Collection.objects.get(slug="new-products")
        on_sale_products = Collection.objects.get(slug="on-sale")
        best_selling_products = Collection.objects.get(slug="best-selling")
        banner = Banner.objects.filter(web=True)
    except:
        new_products =[]
        on_sale_products = []
        best_selling_products = []
        banner = []

    return HttpResponse(
        render(
            request,
            'main_site/screens/home.html',
                {
                'new_products':new_products,
                'on_sale':on_sale_products,
                'best_selling':best_selling_products,
                'banner':banner,
                }
            )
        )



def main_login(request):

    error = False
    msg   = ""

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        try: 
            user = User.objects.get(email=username)
            user = authenticate(username=user.username,password=password)
        except:
            try:
                user = User.objects.get(username=username)
                user = authenticate(username=user.username,password=password)
            except:
                error = True
                msg = "Email or Mobile Number Not Found"
                return HttpResponse(render(request,'main_site/screens/login.html',{"error":error,"msg":msg}))

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('veregood:index'))
        else:
            error = True
            msg = "Incorrct Password"

    return HttpResponse(render(request,'main_site/screens/login.html',{"error":error,"msg":msg}))



def signup(request):
    
    error = False
    err_message = ""
    
    if request.method == 'POST':
        # print(request.POST)
        
        name         = request.POST["name"]
        country_code_mobile_number=request.POST["phone"]
        email        = request.POST["email"]
        password     = request.POST["password"]
        try:
            l= country_code_mobile_number.split(" ")
            country_code =  l[0]
            mobile_number = l[1]
        except:
            error = True
            err_message ="Select Country"
            return HttpResponse(render(request,'main_site/screens/register.html',{"error":error,"msg":err_message}))

        

       
        #     request.session['mobile_number'] = request.POST['username']
        #     request.session['country_code'] = str("+")+request.POST['country_code']
        #     request.session['email'] = request.POST['email']
        #     request.session['password'] = request.POST['password']
        #     request.session['first_name'] = request.POST['first_name']


        #     # return HttpResponseRedirect(reverse('veregood_vendor:user_verification',kwargs={'redirect':'complete_profile'}))
        # Direct Access
        try:
            user = User(
                        username=mobile_number,
                        email=email,
                        country_code=country_code[1:],
                        first_name=name,
                        is_vendor=True,
                        is_staff  = True,
                        
                    )
            # user.has_perm('veregood.add_product')
            # user.has_perm('veregood.change_product')
            # user.has_perm('veregood.view_product')
            user.set_password(request.POST['password'])
            user.save()
        
        
            login(request,user)
            return HttpResponseRedirect(reverse('veregood:index'))
        except:
            error= True
            err_message = "Details Already Exsist"


    return HttpResponse(render(request,'main_site/screens/register.html',{"error":error,"msg":err_message}))













def verification(request):
    return HttpResponse(render(request,'main_site/screens/otp-verification.html'))

@login_required(login_url="veregood:login")
def cart(request):
    cart , created = Cart.objects.get_or_create(user=request.user)


    return HttpResponse(render(request,'main_site/screens/cart.html',{"cart":cart}))

def dashboard(request):
    return HttpResponse(render(request,'main_site/screens/dashboard.html'))

def category(request,pk):
    show = True
    categories = Category.objects.filter(parent=None)
    products= Product.objects.filter(category__id=pk)
    if products.count() == 0:
        show = False
    return HttpResponse(render(request,'main_site/screens/category.html',{"categories":categories,"products":products,"p_count":show}))


def allproducts(request):
    show = True
    categories = Category.objects.filter(parent=None)
    products= Product.objects.all()
    if products.count() == 0:
        show = False
    return HttpResponse(render(request,'main_site/screens/category.html',{"categories":categories,"products":products,"p_count":show}))

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
@csrf_exempt
def product(request,pk):

    # print(product.page_layout)
    if request.method == "POST":
        # print("Hi")
        return HttpResponseRedirect(reverse("veregood:shopping-cart"))
    else:
        product = Product.objects.get(id=pk)
        return HttpResponse(render(request,'main_site/screens/product.html',context={"product":product}))



def update_cart(request):
    cart = Cart.objects.get(user=request.user)
    from django.db.models import Sum
    try:
        sub_total = CartItem.objects.filter(cart__id=cart.id).aggregate(Sum('line_total'))

        cart.sub_total = sub_total["line_total__sum"]
        cart.total=cart.sub_total
        cart.save()
    except:
        cart.sub_total = 0
        cart.total = 0
        cart.save()


def add_cart(request,pk):
    try:
        product =Product.objects.get(id=pk)
        quantity = int(request.POST["quantity"])
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.create(cart=cart,product=product,quantity=quantity,line_total=int(product.price)*quantity)
        update_cart(request)
        return HttpResponseRedirect(reverse("veregood:shopping-cart"))
    except:
        return HttpResponseRedirect(reverse("veregood:login"))


def add_quantity(request,pk):
    cart_item = CartItem.objects.get(id=pk)
    cart_item.quantity=cart_item.quantity+1
    cart_item.line_total = int(cart_item.product.price)*cart_item.quantity
    cart_item.save()
    update_cart(request)
    return HttpResponseRedirect(reverse("veregood:shopping-cart"))

def remove_quantity(request,pk):
    cart_item = CartItem.objects.get(id=pk)
    print(cart_item.quantity)
    if cart_item.quantity == 1:

        CartItem.objects.get(id=pk).delete()
    else:
        cart_item.quantity = cart_item.quantity - 1
        cart_item.line_total = int(cart_item.product.price) * cart_item.quantity
        cart_item.save()

    update_cart(request)

    return HttpResponseRedirect(reverse("veregood:shopping-cart"))
def delete_cart_item(request,pk):
    CartItem.objects.get(id=pk).delete()
    update_cart(request)
    return HttpResponseRedirect(reverse("veregood:shopping-cart"))

def checkout(request):
    from veregood.main_site.forms import AddressForm
    cart = Cart.objects.get(user=request.user)
    if cart.cart_item.all().count() == 0:
        return HttpResponseRedirect(reverse("veregood:shopping-cart"))
    form    = AddressForm()
    address = Address.objects.filter(user=request.user)
    return HttpResponse(render(request,'main_site/screens/checkout.html',{"form":form,"address":address}))

def wishlist(request):
    wishlist , created = Wishlist.objects.get_or_create(user=request.user)
    return HttpResponse(render(request,'main_site/screens/wishlist.html',{"wishlist",wishlist}))



def search(request):
    show = True
    products = Product.objects.all()
    categories = Category.objects.filter(parent=None)
    if request.GET['cat'] == 'all':
        products = products.filter(title__contains=request.GET['q'])
    else:
        products = products.filter(title__contains=request.GET['q'],category__slug=request.GET['cat'])
    if products.count() == 0:
        show = False
    return HttpResponse(render(request,'main_site/screens/category.html',{"categories":categories,"products":products,"p_count":show}))



def services(request):
    from veregood_service.models import VendorService
    q = request.GET["q"]
    services = VendorService.objects.filter(service_type__service_name = q)
    return HttpResponse(render(request,'main_site/screens/services.html',{"services":services}))