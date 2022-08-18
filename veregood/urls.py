from django.contrib import admin
from django.urls import path,include
from veregood.views import *




urlpatterns = [

    # API VERSION 1.0 DEXTER
    path('banner/',                BannerView.as_view()),
    path('collection/',            CollectionView.as_view()),
    path('cart/',                  CartView.as_view()),
    path('wishlist/',              WishlistView.as_view()),
    path('category/',              CategoryView.as_view()),
    path('product/',               ProductView.as_view()),
    path('search/',                SearchView.as_view()),
    path('review/',                ProductReviewView.as_view()),
    path('address/',               AddressView.as_view()),
    path('check-user/',            UserView.as_view()),
    path('register/',              UserView.as_view()),
    path('quoute/',                Quote.as_view()),
    path('auction/',               Auction.as_view()),
    path('explore/',               Explore.as_view()),
    path('collection-group/',      CollectionGroupView.as_view()),
   

]
