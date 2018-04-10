from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def login_page(request):
    return render(request, 'pages/login.html')


def login_check(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/dashboard')
    else:
        return redirect('/')


def user_logout(request):
    logout(request)
    return redirect('/')
