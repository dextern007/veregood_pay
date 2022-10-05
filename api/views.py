from ipaddress import ip_address
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import random
# from account.models import DeviceVerification,User
from rest_framework.authtoken.models import Token
from api.serializer import *
from django.core.files.images import ImageFile





class VendorServiceView(APIView):
    def get(self,request,format=None):
        id= self.request.query_params.get("id")
        vendor_service = VendorService.objects.get(id=id)
        vendor_service_serializer = VendorServiceSerializer(vendor_service)
        return Response(vendor_service_serializer.data, status=status.HTTP_200_OK)


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
        from datetime import datetime as dt
        from dateutil import parser

        data=request.data
        from_date = data["from_date"]
        to_date   = data["to_date"]
        service_id = data["service_id"]
        user_id = data["user_id"]
        vendor_service = VendorService.objects.get(id=service_id)
        charge = vendor_service.charge
        
        ds1 = parser.parse(from_date)
        ds2 = parser.parse(to_date)
        days=(ds2-ds1).days

        fee_calculation = charge*days
        total_charges   = str(fee_calculation*100)

        booking = Booking.objects.create(user_id=user_id,service=vendor_service,from_date=ds1,to_date=ds2,total_amount=total_charges)
        
        return Response({"message":"Booking initiated","fees": fee_calculation,"booking_id":booking.id}, status=status.HTTP_200_OK)






    def get(self,request,format=None):
        id= self.request.query_params.get("id")
        detail= self.request.query_params.get("detail")
        if detail== "false":
            bookings = Booking.objects.filter(user_id=id)
            booking_service_serializer = BookingSerializer(bookings,many=True)
            return Response( booking_service_serializer.data, status=status.HTTP_200_OK)
        else:
            booking = Booking.objects.get(id=id)
            booking_service_serializer = BookingSerializer(booking)
            return Response( booking_service_serializer.data, status=status.HTTP_200_OK)


class RatingView(APIView):

    def post(self,request,format=None):
        serializer= ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
from rest_framework.parsers import MultiPartParser ,FormParser

def modify_input_for_multiple_files(property_id, image):
    dict = {}
    dict['service_id'] = property_id
    dict['image'] = image
    return dict

class CreateVendor(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request,format=None):
        
        data = request.data
        try:
            vendor = Vendor.objects.create(
                first_name = data["first_name"],
                last_name  = data["last_name"],
                nick_name  = data["nick_name"],
                email      = data["email"],
                mobile_number      = data["mobile_number"],
                proof_one  = data["proof_one"],
                proof_two  = data["proof_two"],
            )

            service = VereGoodService.objects.get(service_name=data["service_name"])
            from django.contrib.gis.geos import Point
            vendor_service = VendorService.objects.create(
                vendor            =   vendor,
                service_type      =   service,
                name              =   data["first_name"],
                description       =   data["description"],
                profile_image     =   data["profile_picture"],
                location          =   Point(float(data["longitude"]),float(data["latitude"])),
                charge            =   data["charge"],
            )
            images = dict((request.data).lists())['portfolio_images']
            
            arr = []
            for img_name in images:
                modified_data = modify_input_for_multiple_files(vendor_service.id,img_name)
                file_serializer = PortfolioSerializer(data=modified_data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    arr.append(file_serializer.data)
                else:
                    return Response({"message": "Invalid Immage Data"}, status=status.HTTP_400_BAD_REQUEST)



            return Response({"message": "Vendor Registered Sucessfully","uploaded_images":arr}, status=status.HTTP_200_OK)

        except:
            return Response({"message": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)