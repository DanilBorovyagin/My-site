# myshop/shop/tasks.py
from celery import shared_task
from django.utils import timezone
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import logging
logger = logging.getLogger(__name__)


@shared_task
def send_notification():
    channel_layer = get_channel_layer()
    message = "Скидка 20% на все товары!"
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            "type": "send_notification",
            "message": message
        }
    )
    logger.info(f"Sent notification: {message}")  # Логируем отправленное сообщение

