from django.contrib import admin
from wallet.models import *
# Register your models here.

class CryptoWalletInline(admin.TabularInline):
    model = CryptoWallet
    extra = 0

class WalletAdmin(admin.ModelAdmin):
    inlines = [CryptoWalletInline]
    class Meta():
        model = Wallet

admin.site.register(Transaction)
admin.site.register(Wallet,WalletAdmin)