from urllib import request
from django.shortcuts import render, redirect

from . import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login


def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = forms.UserForm()
    return render(request, 'signup.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/home/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/accounts/home/')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def users_view(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def user_details_view(request, firstname):
    user = User.objects.get(firstname=firstname)
    return render(request, 'user_details.html', {'user': user})


# Create your views here.
