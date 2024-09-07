# shop/views.py

from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'shop/home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('catalog')
    return render(request, 'shop/login.html')


def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Логика для добавления товара в корзину
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 0}
    )
    cart_item.quantity += 1
    cart_item.save()

    return redirect('catalog')  # Перенаправление обратно в каталог

