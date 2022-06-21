
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



    def put(self,request,format=None):
        data  = request.data
        self.calculate_total()
        self.get(request=request)





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
        serializer = ProductReviewSerializer(reviews,many=True)
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


    def put():
        # Update Payment id to the order
        pass




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

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRECT
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRECT
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        order = Order.objects.get(payment_id=payload["payment_id"])
        order.paid = True
        order.save()
        cart = Cart.objects.get(user=order.user)
        cart.user = None
        cart.save()

    return HttpResponse(status=200)
