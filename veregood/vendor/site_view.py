from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from account.models import User
from veregood.models import Category, Order, Product, Store, VendorOrder
from veregood.vendor.forms import VendorProfileEditForm, VendorProfileForm
from django.views.generic.edit import *

@login_required(login_url="veregood:login")
def logout_vendor(request):
    logout(request)
    return HttpResponseRedirect(reverse('veregood:login'))


def login_vendor(request):

    """
    Verifes the user is on our database by authenticating username and password.

    Conditions : If user is authenticated it redirects to | google_otp_verification | else return error message.

    Arguments :
    mobile_number : username of a user.
    password: password of the user

    """

    if request.user.is_authenticated != True :
        message = ""
        if request.method == "POST":
            mobile_number = request.POST['mobile_number']
            password      = request.POST['password']

            user = authenticate(username=mobile_number,password=password)
            if user is not None:
                obj = User.objects.get(username=mobile_number)
                if obj.is_vendor:
                    login(request,user)
                    request.session['mobile_number'] = mobile_number
                    request.session['password'] = password
                    request.session['country_code'] = "+"+obj.country_code

                    # return HttpResponseRedirect(reverse("veregood_vendor:otp-verification"))

                    # Direct access
                    return HttpResponseRedirect(reverse("veregood_vendor:dashboard"))
                
                else:

                    message = "Not allowed to login as vendor"

            else:
                message = "Invalid Credentials"
                data= {"error":True,"message":message}
                HttpResponse(render(request,'veregood/vendor/screens/login.html',{"data":data}))

        data= {"error":False,"message":message}
        return HttpResponse(render(request,'veregood/vendor/screens/login.html',{"data":data}))
    
    else:
        if request.user.is_vendor:
            # logout(request)
            return HttpResponseRedirect(reverse("veregood_vendor:dashboard"))

        else:
            logout(request)
            message = "Invalid Credentials"
            data= {"error":True,"message":"Not allowed to login as vendor"}
            return HttpResponse(render(request,'veregood/vendor/screens/login.html',{"data":data}))



# OTP Verification #######
def google_otp_verification(request):
    
    if request.method == "POST":
        mobile_number = request.session['mobile_number']
        password      = request.session['password']

        user = authenticate(username=mobile_number,password=password)
        if user is not None:
            obj = User.objects.get(username=mobile_number)
            if obj.is_vendor:
                login(request,user)
                return HttpResponseRedirect(reverse("veregood_vendor:dashboard"))
            
            else:

                message = "Not allowed to login as vendor"

        else:
            message = "Invalid Credentials"
            data= {"error":True,"message":message}
            HttpResponse(render(request,'veregood/vendor/screens/login.html',{"data":data}))
       

    return HttpResponse(render(request,'veregood/vendor/screens/otp-verification.html'))
  
def forgot_password_otp_verification(request):
    message = ""
    if request.method == "POST":
        return HttpResponseRedirect(reverse("veregood_vendor:update-password"))
        

    return HttpResponse(render(request,'veregood/vendor/screens/forgot-password.html',{"message":message}))
# OTP Verification #######


def update_password(request):
    """
    The Functions lets to update the password of current user with session datas after otp verification done.
    """

    if request.method == "POST":
        obj = User.objects.get(username=request.session["mobile_number"])
        obj.set_password(request.POST["password"])
        obj.save()
        user=authenticate(username=obj.username,password=request.POST["password"])
        login(request,user)
        return HttpResponseRedirect(reverse("veregood_vendor:dashboard"))

    return HttpResponse(render(request,'veregood/vendor/screens/update-password.html'))


def verify_vendor_availabilty(request):
    message=""
    if request.method == "POST":
        mobile_number = request.POST['mobile_number']
        try:
            obj = User.objects.get(username=mobile_number)
            if obj.is_vendor:
                request.session['mobile_number'] = mobile_number
                request.session['country_code'] = obj.country_code  
                return HttpResponseRedirect(reverse("veregood_vendor:forgot-password"))

            else:
                message = "User is not vendor"
        except:
            message = " User Not Available"


    return HttpResponse(render(request,'veregood/vendor/screens/check-user.html',{"message":message}))



def register(request):
    """
        This Function will Register a user as vendor
    """


    from veregood.vendor.forms import VendorForm
    form = VendorForm()
    if request.method == 'POST':
        form = VendorForm(request.POST)

        if form.is_valid():
            request.session['mobile_number'] = request.POST['username']
            request.session['country_code'] = str("+")+request.POST['country_code']
            request.session['email'] = request.POST['email']
            request.session['password'] = request.POST['password']
            request.session['first_name'] = request.POST['first_name']


            # return HttpResponseRedirect(reverse('veregood_vendor:user_verification',kwargs={'redirect':'complete_profile'}))



            # Direct Access
            user = User(
                        username=request.session['mobile_number'],
                        email=request.session['email'],
                        country_code=request.session['country_code'][1:],
                        first_name=request.session['first_name'],
                        is_vendor=True,
                        is_staff  = True,
                        
                    )
            # user.has_perm('veregood.add_product')
            # user.has_perm('veregood.change_product')
            # user.has_perm('veregood.view_product')
            user.set_password(request.session['password'])
            user.save()
            
            
            login(request,user)
            return HttpResponseRedirect(reverse('veregood_vendor:complete_profile'))



 
    return HttpResponse(render(request,'veregood/vendor/screens/register.html',{'form':form}))



# OTP VERIFICATION
def user_verification(request,redirect):

    if request.method == 'POST':
        if redirect == 'complete_profile':
            user = User(
                        username=request.session['mobile_number'],
                        email=request.session['email'],
                        country_code=request.session['country_code'][1:],
                        first_name=request.session['first_name'],
                        is_vendor = True,
                        is_staff  = True,
                    )
            
            user.set_password(request.session['password'])
            user.save()
            login(request,user)
            return HttpResponseRedirect(reverse('veregood_vendor:'+redirect))

    
    
    return HttpResponse(render(request,'veregood/vendor/screens/auth/otp-verification.html',{'redirect':redirect}))
# OTP VERIFICATION


@login_required
def complete_profile(request):
    """
    This Function used to create a vendor profile and add permissions to the vendor

    Arguments : Vendor Inofrmations
    """
    
    form = VendorProfileForm()

    if request.user.is_vendor == False:
        return HttpResponseRedirect(reverse('veregood:index'))
    
    if request.method == "POST":
        form = VendorProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new_form         = form.save(commit=False)
            new_form.user    = request.user
            new_form.store_setup    = True
            new_form.save()
            user = User.objects.get(id=request.user.id)
            from django.contrib.auth.models import Permission
            
            user.user_permissions.add(

                Permission.objects.get(codename='add_product'),
                Permission.objects.get(codename='change_product'),
                Permission.objects.get(codename='view_product'),

                Permission.objects.get(codename='add_productimage'),
                Permission.objects.get(codename='change_productimage'),
                Permission.objects.get(codename='view_productimage'),
                Permission.objects.get(codename='delete_productimage'),
                
                Permission.objects.get(codename='add_variationgroup'),
                Permission.objects.get(codename='change_variationgroup'),
                Permission.objects.get(codename='view_variationgroup'),
                Permission.objects.get(codename='delete_variationgroup'),

                Permission.objects.get(codename='add_productdescription'),
                Permission.objects.get(codename='change_productdescription'),
                Permission.objects.get(codename='view_productdescription'),

                Permission.objects.get(codename='add_variation'),
                Permission.objects.get(codename='change_variation'),
                Permission.objects.get(codename='view_variation'),
                Permission.objects.get(codename='delete_variation'),

                Permission.objects.get(codename='add_producttab'),
                Permission.objects.get(codename='change_producttab'),
                Permission.objects.get(codename='view_producttab'),
                Permission.objects.get(codename='delete_producttab'),
                )

            user.save()
            return HttpResponseRedirect(reverse('veregood_vendor:dashboard'))

    

    return HttpResponse(render(request,'veregood/vendor/screens/complete-profile.html',{'form':form}))



@login_required(login_url="veregood:login")
def dashboard(request):
    if request.user.is_vendor == False:
        return HttpResponseRedirect(reverse('veregood:index'))

    try:
        request.user.store 
    except:
        return HttpResponseRedirect(reverse('veregood_vendor:complete_profile'))
    
    if request.user.store.store_setup == None:
        return HttpResponseRedirect(reverse('veregood_vendor:complete_profile'))


    return HttpResponse(render(request,'veregood/vendor/screens/dashboard.html'))




@login_required(login_url="veregood:login")
def select_category(request):

    """
    Selecting a category Before Adding Product
    """

    id = request.GET["category_id"]
    prod_type = request.GET["type"]

    if id == "0":
        categories = Category.objects.filter(parent=None)

    else:
        category = Category.objects.get(id=id)
        categories = Category.objects.filter(parent=category)
        if len(categories) == 0:
            product=Product(store=Store.objects.get(user=request.user),category=category,product_type=prod_type)
            product.save()


            return HttpResponseRedirect(reverse('vendor_admin:veregood_product_change',args=[product.id]))


    return HttpResponse(render(request,'veregood/vendor/screens/dashboard/select-category.html',{"categories":categories,"type":prod_type}))


@login_required(login_url="veregood:login")
def product_view(request):


    """
    List of products with filters of approved and un_approved
    """
    try:

        filter_q = request.GET["filter"]

        if filter_q == "approved":
            products = Product.objects.filter(store=Store.objects.get(user=request.user),is_approved=True)
        elif filter_q == "unapproved":
            products = Product.objects.filter(store=Store.objects.get(user=request.user),is_approved=False)
        elif filter_q == "draft":
            products = Product.objects.filter(store=Store.objects.get(user=request.user),draft=True)
        elif filter_q == "all":
            products = Product.objects.filter(store=Store.objects.get(user=request.user))

        else:
            products = Product.objects.filter(store=Store.objects.get(user=request.user))
            
    except:
        products = Product.objects.filter(store=Store.objects.get(user=request.user))

    return HttpResponse(render(request,'veregood/vendor/screens/dashboard/product.html',{"products":products}))



@login_required(login_url="veregood:login")
def store_setting(request):
    
    
    form = VendorProfileEditForm()
    return HttpResponse(render(request,'veregood/vendor/screens/dashboard/store.html',{"form":form}))


@login_required(login_url="veregood:login")
def order_list(request): 
    order = VendorOrder.objects.filter(vendor=request.user)
    return HttpResponse(render(request,'veregood/vendor/screens/dashboard/order.html',{"orders":order}))