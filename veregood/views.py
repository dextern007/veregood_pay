
from django.conf import settings
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView
from account.models import User
from veregood.serializer import *
from veregood.models import*
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
# Create your views here.


# Listing all Banners for mobile
class BannerView(APIView):
    
    def get(self,request,format=None):
        device = self.request.query_params.get('device',None)
        banners = Banner.objects.filter(is_active=True)
        if device == "mobile":
            banners= banners.filter(mobile=True)
        else:
            banners= banners.filter(web=True)

        serializer = BannerSerilaizer(banners,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class CollectionView(APIView):

    # Get Collections List
    def get(self,request,format=None):
        collections = Collection.objects.filter(is_active=True)
        serializer = CollectionSerializer(collections,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # Get List of products in collections
    def post(self,request,format=None):
        collection = Collection.objects.get(slug=request.data["id"])
        products   = ProductListing.objects.filter(collection=collection)
        serializer = ListingSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    


class CartView(APIView):
    authentication_classes = [TokenAuthentication]

    def calculate_total(data):
        # saves total and line total
        pass
    

    def get(self,request,format=None):
        user = request.user
        # print(user)
        cart , created = Cart.objects.get_or_create(user=user)
        serializer = CartSerializer(cart)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def add_item_to_cart(self,data):
        user = self.request.user
        cart , created = Cart.objects.get_or_create(user=user)
        cart_item = CartItem(cart=cart,
        product = Product.objects.get(id=data["product_id"]),
        has_variation = data["has_variation"],
        quantity = int(data["quantity"])
        )
        if data["has_variation"]==True:
            cart_item.variation.add(Variation.objects.filter(id__in=data["variations"]))

        cart_item.save()

        return {"message":"Item Added Successfully","cart_item":CartItemSerializer(cart_item).data}


    def remove_item_from_cart(self,data):
        CartItem.objects.get(id=data["cart_item_id"]).delete()
        return {"message":"Item Removed Successfully"}

    def update_cart_item_quantity(self,data):
        user = self.request.user
        if int(data["quantity"]) == 0:
            resp = self.remove_item_from_cart(data)
            return resp
        else:
            cart_item = CartItem.objects.get(id=data["cart_item_id"])
            cart_item.quantity = int(data["quantity"])

            return {"message":"Item Added Successfully","cart_item":CartItemSerializer(cart_item).data}

    def put(self,request,format=None):
        method = self.request.query_params.get('method',None)
        data  = request.data
        if method == "add":
            resp = self.add_item_to_cart(data=data)

        elif method =="remove":
            resp = self.remove_item_from_cart(data=data)

        else:
            resp = self.update_cart_item_quantity(data=data)

        return Response(resp,status=status.HTTP_200_OK)



class WishlistView(APIView):
    authentication_classes = [TokenAuthentication]  

    def get(self,request,format=None):
        user = request.user
        try:
            wishlist = Wishlist.objects.get(user=user)
        except: 
            wishlist = Wishlist.objects.create(user=user)
            
        serializer = WishListSerializer(wishlist)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,format=None):
        product = Product.objects.get(id=request.data["id"])
        item    = WishlistItem.objects.create(product=product,wishlist=request.user.wishlist)
        return Response({"message":" Product added successfully"},status=status.HTTP_200_OK)

    def delete(self,request,format=None):
        item = WishlistItem.objects.get(id=request.data["id"])
        item.delete()
        return Response({"message":" Product Removed successfully"},status=status.HTTP_200_OK)



class CategoryView(APIView):

    def get(self,request,format=None):
        flag = self.request.query_params.get('id',None)

        if flag == "0":
            categories = Category.objects.filter(parent=None)
        else:
            categories = Category.objects.filter(parent=Category.objects.get(id=flag))


        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,format=None): 
        data = []
        categories = Category.objects.filter(parent=None)
        for category in categories:
            main_cat = CategorySerializer(category).data
            sub      = Category.objects.filter(parent=category)
            sub_cat  = CategorySerializer(sub,many=True).data
            main_cat["sub_category"]=sub_cat
            data.append(main_cat)
        return Response(data,status=status.HTTP_200_OK)


    def post(self,request,format=None):
        category = Category.objects.get(id=request.data["id"])
        serializer = CategoryProductSerializer(category)
        return Response(serializer.data,status=status.HTTP_200_OK)






class ProductView(APIView):
    def get(self,request,format=None):
        id = self.request.query_params.get('id',None)
        product = Product.objects.get(id=id)
        serializer = ProductDetail(product)
        return Response(serializer.data,status=status.HTTP_200_OK)




class ProductReviewView(APIView):

    def get(self,request,format=None):
        product_id = self.request.query_params.get('product_id',None)
        reviews = ProductReview.objects.filter(product__id = product_id)
        serializer = ProductReviewListSerializer(reviews,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = ProductReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






class OrderView(APIView):
    authentication_classes = [TokenAuthentication]
    def get(self,request,format=None):
        order_id = self.request.query_params.get("id",None)
        
        if order_id is None:
            # get all orders of a user
            orders = Order.objects.filter(user=request.user)
            serializer = OrderSerializer(orders,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            # get specific order in detail
            order = Order.objects.get(id=order_id)
            serializer = OrderSerializer(order)
            return Response(serializer.data,status=status.HTTP_200_OK)

        
        
    def post(self,request,format=None):
        # Create an Order 
        cart        = Cart.objects.get(user=request.user)
        order       = Order.objects.create(user=request.user,cart=cart)
        order.total = cart.total

        # total+tax+delivery_charge - discount
        order.final_total = cart.total
        order.save()

        # Create Payment Intent
        pass


    def put(self,request,format=None):
        data = request.data
        order = Order.objects.get(id=data["1d"])
        order.payment_id = data["payment_id"]
        order.save()

        




class AddressView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self,request,format=None):
        addresses = Address.objects.filter(user=request.user)
        serializer = AddressSerilaizer(addresses,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request,format=None):
        serializer = AddressSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,format=None):
        pk = self.request.query_params.get('id',None)
        address = Address.objects.get(id=pk)
        serializer = AddressSerilaizer(address,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,format=None):
        pk = self.request.query_params.get('id',None)
        address = Address.objects.get(id=pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SearchView(APIView):

    def post(self,request,format=None):
        keyword = request.data["keyword"]
        products = Product.objects.filter(title__icontains = keyword)
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserView(APIView):
    def get(self,request,format=None):
        mobile_number = self.request.query_params.get("mobile_number")
        try:
            user=User.objects.get(username=mobile_number)
            token ,created = Token.objects.get_or_create(user=user)


            data = {
                "profile": {
                    "name" : user.first_name,
                    "email" : user.email,
                    "mobile_number" : user.mobile_number,
                    "country_code" : user.country_code,
                },
                "token":token.key
            }
            return Response(data,status=status.HTTP_200_OK)

        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
       

    def post(self,request,format=None):
        import random
        username = request.data["username"]
        name = request.data["name"]
        email = request.data["email"]
        country_code = request.data["country_code"]
        user=User(first_name=name,username=username,mobile_number=username,email=email,country_code=country_code)
        user.set_password(str(random.randint(1000000000000,9999999999999999)))
        user.save()
        token ,created = Token.objects.get_or_create(user=user)


        data = {
            "profile": {
                "name" : user.first_name,
                "email" : user.email,
                "mobile_number" : user.mobile_number,
                "country_code" : user.country_code,
            },
            "token":token.key
        }
        return Response(data,status=status.HTTP_200_OK)


class Quote(APIView):

    def get(self,request,format=None):
        quotes= Quote.objects.filter(user=request.user)
        serializer = QuoteSerializer(quotes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        data = request.data
        try:
            quote = Quote(
                product=Product.objects.get(id=data["product_id"]),
                user = request.user,
                contact_email = data["contact_email"],
                contact_mobile = data["contact_mobile"],  
                )
            quote.save()
            serializer=QuoteSerializer(quote)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"Invalid Data"},status=status.HTTP_400_BAD_REQUEST)
            




class Auction(APIView):
    def get(self,request,format=None):
        auctions= Auction.objects.filter(user=request.user)
        serializer = AuctionSerializer(auctions,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        data = request.data
        try:
            auction = Auction(
                product=Product.objects.get(id=data["product_id"]),
                user = request.user,
                bid_amount = data["bid_amount"]
                )
            auction.save()
            serializer=QuoteSerializer(auction)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"Invalid Data"},status=status.HTTP_400_BAD_REQUEST)



class Explore(APIView):
    def get(self,request,format=None):
        explores = Explore.objects.filter(active=True)
        serializer = ExploreSerializer(explores,many=True) 
        return Response(serializer.data,status=status.HTTP_200_OK)




class CollectionGroupView(APIView):
    def get(self,request,format=None):
        collection_groups = CollectionGroup.objects.filter(active=True)
        serializer = CollectionGroupSerializer(collection_groups,many=True) 
        return Response(serializer.data,status=status.HTTP_200_OK)
