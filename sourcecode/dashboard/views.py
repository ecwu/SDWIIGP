from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'dashboard/index.html')


def user_info(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'dashboard/user.html')
