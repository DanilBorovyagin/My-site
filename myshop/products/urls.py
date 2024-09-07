# products/urls.py

from django.urls import path
from .views import add_to_cart, cart

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
]