from django.contrib import admin
from currency.models import *
# Register your models here.

admin.site.register(Currency)
admin.site.register(ExchangeRate)
