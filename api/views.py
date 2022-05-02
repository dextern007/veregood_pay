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
    def get(self,request):
        id= self.request.query_params.get("id")
        vendor_service = VendorService.objects.get(id=id)
        vendor_service_serializer = VendorServiceSerializer(vendor_service)
        return Response( vendor_service_serializer.data, status=status.HTTP_200_OK)