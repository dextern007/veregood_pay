from django import forms
from  veregood.models import Address
class AddressForm(forms.ModelForm):
    class Meta():
        model  = Address
        exclude = ["user","location"]