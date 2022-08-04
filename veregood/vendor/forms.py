from django import forms
from account.models import User
from veregood.models import *
from mapwidgets.widgets import GooglePointFieldWidget





# To Register Vendor
class VendorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["first_name","username","email","country_code","password"]
        labels = {
        "username": "Enter Your mobile Number",
        "first_name": "Enter Your Name",
        "email": "Enter Your Email Address",
        "password": "Create a new password",
        "country_code": "Select Your Country",
         }
        help_texts = {
            'username': 'Enter Mobile Number Without Country Code',
            'country_code': '*Required',
        }
        

    
    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)

        # Form Class
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['country_code'].widget.attrs.update({'class': 'form-control','id':'exampleSelectGender'})
        self.fields['password'].widget.attrs.update({'class': 'form-control form-control-lg'})

        self.fields['username'].required = True
        self.fields['country_code'].required = True
        self.fields['first_name'].required = True





   
    
   
    
   

   

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = Store
        fields =['logo','store_name','store_describtion','contact_mobile_number','contact_email','address','city','state','country',"available_regions","base_currency"]
        labels = {
            'logo' : ' Your Store Logo',
            'store_name' : 'Enter the store name',
            'store_describtion' : 'Short describtion of your store',
            'contact_mobile_number' : 'Contact Phone Number',
            'contact_email' : 'Contact Email',
            'address' : 'Your Address',
            'city': 'Your City',
            'state':'Your State',
            'country' : ' Your Country',
            'available_regions' : 'Availanlity Region',
            'base_currency' : 'Store Base Currency',

         }
        help_texts = {
          'address' : ' The Address, city, State of the store'
        }
        

    def __init__(self, *args, **kwargs):
        super(VendorProfileForm, self).__init__(*args, **kwargs)

        # Form Class
        self.fields['logo'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['store_name'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['store_describtion'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['contact_mobile_number'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['contact_email'].widget.attrs.update({'class': 'form-control form-control-lg','type':'email'})
        self.fields['address'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['city'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['state'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['country'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['available_regions'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['base_currency'].widget.attrs.update({'class': 'form-control form-control-lg'})
        
        # Required fields
        self.fields['logo'].required = False
        self.fields['store_name'].required = True
        self.fields['store_describtion'].required = True
        self.fields['contact_mobile_number'].required = True
        self.fields['contact_email'].required = True
        self.fields['address'].required = True
        self.fields['city'].required = True
        self.fields['state'].required = True
        self.fields['country'].required = True
        self.fields['country'].required = True
        self.fields['base_currency'].required = True
        self.fields['available_regions'].required = True

from mapwidgets.widgets import GooglePointFieldWidget

CUSTOM_MAP_SETTINGS = {
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocation", [60.7177013, -22.6300491]),
    ),
}

class VendorProfileEditForm(forms.ModelForm):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget(settings=CUSTOM_MAP_SETTINGS)}
    }
    class Meta:
        model = Store
        exclude =["vendor_id","user","closed","is_active","store_setup","is_approved","kyc_verified","payment_method_added","upi_id","aadhar_number","profile_picture","dob","age","pan_number"]

    def __init__(self, *args, **kwargs):
        super(VendorProfileEditForm, self).__init__(*args, **kwargs)

        # Form Class
        # self.fields['vendor_id'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['logo'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['store_name'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['store_describtion'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['contact_mobile_number'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['contact_email'].widget.attrs.update({'class': 'form-control form-control-sm','type':'email'})
        self.fields['address'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['city'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['state'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['country'].widget.attrs.update({'class': 'form-control form-control-sm'})
        
        # Required fields
        self.fields['logo'].required = False
        self.fields['store_name'].required = True
        self.fields['store_describtion'].required = True
        self.fields['contact_mobile_number'].required = True
        self.fields['contact_email'].required = True
        self.fields['address'].required = True
        self.fields['city'].required = True
        self.fields['state'].required = True
        self.fields['country'].required = True