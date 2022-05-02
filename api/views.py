from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import random
from account.models import DeviceVerification,User
from rest_framework.authtoken.models import Token
from api.serializer import *
import io
from django.core.files.images import ImageFile

class VerifyMobile(APIView):

    def send_otp(self,mobile_number,country_code):
        pass

    def generate_otp(self):
        return random.randint(1000,9999)

    def get(self,request):
        session_id = self.request.query_params.get("session_id")
        device = DeviceVerification.objects.get(id=int(session_id))

        try:

            user = User.objects.get(mobile_number=device.mobile_number)
            token , created = Token.objects.get_or_create(user=user)

            return Response({"token":token.key,"kyc":user.kyc_verified},status=status.HTTP_200_OK)

        except:
            return  Response({"message": "New User"},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        data          = request.data
        mobile_number = data["mobile_number"]
        ip_address    = data["ip_address"]
        country_code  = data["country_code"]
        try:
            otp = self.generate_otp()
            self.send_otp(mobile_number,country_code)
            print(otp)
            device = DeviceVerification.objects.create(mobile_number=mobile_number,ip_address=ip_address,otp=otp)
            return Response({"message":"Otp Sent Successfully","session_id":device.id},status=status.HTTP_200_OK)

        except:
            return Response({"message": "Retry !"},status=status.HTTP_403_FORBIDDEN)

    def post(self,request):
        data          = request.data
        session_id = data["session_id"]
        otp    = data["otp"]
        ip_address    = data["ip_address"]

        try:
            device = DeviceVerification.objects.get(id=session_id)
            if device.ip_address == ip_address and device.otp == otp :

                return Response({"message":"Otp Verified Successfully"},status=status.HTTP_200_OK)

            else:
                return Response({"message": "Invalid details"},status=status.HTTP_400_BAD_REQUEST)

            # return Response({"message": "Retry !"}, status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({"message": "Retry !"},status=status.HTTP_403_FORBIDDEN)






class AuthView(APIView):

    def generate_username(self,first_name,mobile):
        return first_name+"-"+mobile

    def post(self,request):
        data = request.data

        password = make_password(password=str(random.randint(10000000000,9000000000000)))
        # image = ImageFile(io.StringIO(data["image"]), name=data["first_name"]+".png")
        try:
            user = User.objects.create(username=self.generate_username(data["first_name"],data["mobile"]),
                                       password= password,email=data["email"],
                                       first_name=data["first_name"],
                                       last_name=data["last_name"],
                                       mobile_number=data["mobile"],
                                       )
            try:
                user.image = data["image"]
            except:
                pass

            user.set_password(str(password))

            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "kyc": user.kyc_verified}, status=status.HTTP_200_OK)


        except:
            return Response({"message": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)



class VendorServiceView(APIView):
    def get(self,request,format=None):
        id= self.request.query_params.get("id")
        vendor_service = VendorService.objects.get(id=id)
        vendor_service_serializer = VendorServiceSerializer(vendor_service)
        return Response( vendor_service_serializer.data, status=status.HTTP_200_OK)


class BookingView(APIView):

    def put(self,request,format=None):
        data=request.data
        booking_id = data["booking_id"]
        payment_id = data["payment_id"]
        booking = Booking.objects.get(id=booking_id)
        booking.payment_id = payment_id
        booking.payment_completed = True
        booking.save()
        return Response({"message":"Booked Successfully"}, status=status.HTTP_200_OK)

    def post(self,request,format=None):


        from datetime import datetime
        data=request.data
        from_date = data["from_date"]
        to_date   = data["to_date"]
        service_id = data["service_id"]
        user_id = data["user_id"]
        vendor_service = VendorService.objects.get(id=service_id)
        charge = vendor_service.charge
        date_format = "%m/%d/%Y"
        a = datetime.strptime(from_date, date_format)
        b = datetime.strptime(to_date, date_format)
        delta = b - a
        days = delta.days

        fee_calculation = charge*days
        total_charges   = str(fee_calculation*100)
        booking = Booking(user_id=user_id,service=vendor_service,from_date=from_date,to_date=to_date,total_amount=total_charges)
        booking.save()
        return Response({"message":"Booking initiated"}, status=status.HTTP_200_OK)






    def get(self,request,format=None):
        id= self.request.query_params.get("id")
        bookings = Booking.objects.filter(user_id=id)
        booking_service_serializer = BookingSerializer(bookings,many=True)
        return Response( booking_service_serializer.data, status=status.HTTP_200_OK)


class RatingView(APIView):

    def post(self,request,format=None):
        serializer= ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


