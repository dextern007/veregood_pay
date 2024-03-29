"""veregood_pay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from django.conf import settings
from veregood.admin import vendor_admin_site


urlpatterns = [

    
    path('admin/', admin.site.urls),
    path('vendor-panel/', vendor_admin_site.urls),
    path("api/",include('api.urls')),
    path("socket/",include('chat.urls')),
    path("",include('veregood.main_site.urls')),
    path('veregood/vendor/', include('veregood.vendor.urls'),name="vendor"),
    path('veregood/payment/', include('veregood.payment.urls'),name="payment"),

    # path("stripe/end-point",stripe_webhook,name="stripe_webhook")

    path('tinymce/', include('tinymce.urls')),
    path('_nested_admin/', include('nested_admin.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('web/', include('website.urls')),

              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
