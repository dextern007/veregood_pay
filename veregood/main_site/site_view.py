import email
from cv2 import error
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from account.models import User
from veregood.models import Banner, Cart, Category, Collection, Product, Store, Wishlist
from veregood.vendor.forms import VendorProfileEditForm, VendorProfileForm
from django.views.generic.edit import *



def index(request):
    new_products = Collection.objects.get(slug="new-products")
    on_sale_products = Collection.objects.get(slug="on-sale")
    best_selling_products = Collection.objects.get(slug="best-selling")
    banner = Banner.objects.filter(web=True)
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

def cart(request):
    cart , created = Cart.objects.get_or_create(user=request.user)
    return HttpResponse(render(request,'main_site/screens/cart.html',{"cart",cart}))

def dashboard(request):
    return HttpResponse(render(request,'main_site/screens/dashboard.html'))

def category(request):
    return HttpResponse(render(request,'main_site/screens/category.html'))


def product(request,pk):
    product = Product.objects.get(id=pk)
    print(product.page_layout)
    return HttpResponse(render(request,'main_site/screens/product.html',{"product":product}))



def checkout(request):
    return HttpResponse(render(request,'main_site/screens/checkout.html'))

def wishlist(request):
    wishlist , created = Wishlist.objects.get_or_create(user=request.user)
    return HttpResponse(render(request,'main_site/screens/wishlist.html',{"wishlist",wishlist}))

def services(request):
    return HttpResponse(render(request,'main_site/screens/services.html'))