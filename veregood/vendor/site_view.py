
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from account.models import User




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
                    request.session['country_code'] = obj.country_code
                    return HttpResponseRedirect(reverse("veregood_vendor:otp-verification"))
                
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
            logout(request)
            return HttpResponseRedirect(reverse("veregood_vendor:dashboard"))

        else:
            message = "Invalid Credentials"
            data= {"error":True,"message":"Not allowed to login as vendor"}
            return HttpResponse(render(request,'veregood/vendor/screens/login.html',{"data":data}))



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



def update_password(request):

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
    return HttpResponse(render(request,'veregood/vendor/screens/register.html'))


@login_required(login_url="veregood_vendor:login")
def dashboard(request):
    return HttpResponse(render(request,'veregood/vendor/screens/dashboard.html'))
