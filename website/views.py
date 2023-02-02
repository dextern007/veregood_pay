from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication

from website.models import Page,JsonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from website.models import Api
from rest_framework import status
from rest_framework import serializers
# Create your views here.
def get_page(key):
    return Page.objects.get(key=key)


def PageView(request,key):

    data         = dict()
    print(key)
    try:
        if key == "favicon.ico":
            data["page"] = get_page("index")

        else:
            data["page"] = get_page(key)

    except:
        data["page"] = Page.objects.create(
            key="index",
            title="Home"
        )


    return render(
        request,
        template_name="website/page.html",
        context=data
    )



class ApiRequest(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self,request,format=None):
        global response
        global resp_code
        response = dict()
        resp_code = status.HTTP_204_NO_CONTENT
        api_key = self.request.query_params.get("api_key", None)
        api = Api.objects.get(key=api_key)
        serializer_class = JsonSerializer.objects.filter(api__id=api.id)

        serializer_content = []
        serializer_header = []
        for data in serializer_class:
            serializer_content.append(data.content)
            serializer_header.append(data.headers)

        exec(api.headers, globals())
        exec("\n".join(serializer_header), globals())
        exec("\n".join(serializer_content), globals())
        exec(api.content, locals(), globals())


        return Response(response,status=resp_code)

    def post(self, request, format=None):
        global response
        global  resp_code
        response = dict()
        resp_code = status.HTTP_204_NO_CONTENT
        api_key = self.request.query_params.get("api_key", None)
        api = Api.objects.get(key=api_key)
        serializer_class = JsonSerializer.objects.filter(api__id=api.id)

        serializer_content = []
        serializer_header = []
        for data in serializer_class:
            serializer_content.append(data.content)
            serializer_header.append(data.headers)

        exec(api.headers,globals())
        exec("\n".join(serializer_header), globals())
        exec("\n".join(serializer_content), globals())
        exec(api.content,locals(),globals())
        return Response(response, status=resp_code)

    def put(self,request,format=None):
        global response
        global resp_code
        response = dict()
        resp_code = status.HTTP_204_NO_CONTENT
        api_key = self.request.query_params.get("api_key", None)
        api = Api.objects.get(key=api_key)
        serializer_class = JsonSerializer.objects.filter(api__id=api.id)

        serializer_content = []
        serializer_header = []
        for data in serializer_class:
            serializer_content.append(data.content)
            serializer_header.append(data.headers)

        exec(api.headers, globals())
        exec("\n".join(serializer_header), globals())
        exec("\n".join(serializer_content), globals())
        exec(api.content, locals(), globals())
        return Response(response,status=resp_code)

    def delete(self,request,format=None):
        global response
        global resp_code
        response = dict()
        resp_code = status.HTTP_204_NO_CONTENT
        api_key = self.request.query_params.get("api_key", None)
        api = Api.objects.get(key=api_key)
        serializer_class = JsonSerializer.objects.filter(api__id=api.id)

        serializer_content = []
        serializer_header = []
        for data in serializer_class:
            serializer_content.append(data.content)
            serializer_header.append(data.headers)

        exec(api.headers, globals())
        exec("\n".join(serializer_header), globals())
        exec("\n".join(serializer_content), globals())
        exec(api.content, locals(), globals())
        return Response(response,status=resp_code)