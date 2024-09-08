# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import path
# from myshop.accounts.consumers import AccountsConsumer
# from myshop.products import CartConsumer
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
#
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             [
#                 path("ws/accounts/", AccountsConsumer.as_asgi()),
#                 path("ws/products/cart/", CartConsumer.as_asgi()),
#             ]
#         )
#     ),
# })


import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from shop import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})