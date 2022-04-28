# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance  
from veregood_service.models import VendorService
from api.serializer import *





class ChatConsumer(WebsocketConsumer):

    # Returns ther services surounded by the passed latitude & longtitude 
    def get_services(self,data):
        radius = 5
        coordinates = json.loads(data["message"])
        latitude  = coordinates['latitude']
        longitude = coordinates['longitude']
        
        point = Point(longitude,latitude)    
        services = VendorService.objects.filter(location__distance_lt=(point, Distance(km=radius)))
        serializers = VereGoodServiceListing(services,many=True)
        content = {
            'message': json.dumps(serializers.data)
        }
        self.send_message(content)

    def ack(self,data):
        pass


    commands={

        'veregood_get_services' : get_services,
        'veregood_ack' : ack,

    }
    

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self,data)
       
       
    def send_message(self,data):  
       
        message = data['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))