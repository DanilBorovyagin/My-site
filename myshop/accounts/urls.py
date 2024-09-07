# accounts/urls.py

from django.urls import path
from .views import register
from .views import account_view

urlpatterns = [
    path('register/', register, name='register'),
    path('account/', account_view, name='account'),
]
