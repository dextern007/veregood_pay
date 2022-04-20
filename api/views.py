from django.shortcuts import render
from rest_framework.views import APIView




class AuthView(APIView):

    def login(self):
        pass
    def register(self):
        pass
    def verify(self):
        pass

    def post(self,request,format=None):
        authentication = self.verify(request.data)
        if authentication["login"]==True:
            return Response()
