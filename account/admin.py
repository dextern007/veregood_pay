from django.contrib import admin
from account.models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(BANKDETAIL)
admin.site.register(UPI)
admin.site.register(KYC)
admin.site.register(CryptoAddress)
admin.site.register(DeviceVerification)
admin.site.register(User)