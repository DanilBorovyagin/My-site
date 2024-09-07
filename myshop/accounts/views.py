# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from allauth.account.utils import complete_signup


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserRegistrationForm(
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def account_view(request):
    return render(request, 'accounts/account.html', {'user': request.user})

