from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request, 'pages/login.html')


def login_check(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Login successfully.')
        return redirect('/dashboard')
    else:
        messages.add_message(request, messages.ERROR, 'Wrong username or password.')
        return redirect('/')


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout successfully.')
    return redirect('/')
