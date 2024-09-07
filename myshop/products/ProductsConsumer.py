from channels.generic.websocket import AsyncWebsocketConsumer
import json


class CartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({
            'message': 'This is a WebSocket message.'
        }))
