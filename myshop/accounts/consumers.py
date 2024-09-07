from channels.generic.websocket import AsyncWebsocketConsumer
import json


class AccountsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data: str) -> None:
        # Декодирование данных JSON
        data = json.loads(text_data)

        # Здесь вы можете обработать данные, например:
        message = data.get('data', 'No data sent')

        # Отправка ответа обратно клиенту
        await self.send(text_data=json.dumps({
            'message': f'Data received: {message}'
        }))
