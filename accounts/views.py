from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home_app:index')
    return render(request, 'accounts/forms.html', {'form': form, 'title': 'Login'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, email=email, password=password)
        login(request, new_user)
        return redirect('home_app:index')
    return render(request, 'accounts/forms.html', {'form': form, 'title': 'Register'})


def logout_view(request):
    logout(request)
    return redirect('home_app:index')


def profile(request):
    username = None
    if request.user.is_authenticated:
        context = {
            'username': request.user.username,
            'email': request.user.email,
        }
    return render(request, 'accounts/profile.html', {'context': context})
