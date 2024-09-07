from django.shortcuts import render, redirect
from .models import Product, CartItem
from .forms import CartItemForm
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if request.method == 'POST':
        form = CartItemForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            return redirect('cart')  # Замените на ваш URL для корзины
    else:
        form = CartItemForm(instance=cart_item)

    return render(request, 'products/add_to_cart.html', {'form': form, 'product': product})


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'products/cart.html', {'cart_items': cart_items})


def catalog(request):
    products = Product.objects.all()
    return render(request, 'products/catalog.html', {'products': products})

