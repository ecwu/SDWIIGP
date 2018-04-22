from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def operation_checkin(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'operation/index.html')


def operation_recharge(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'operation/recharge.html')
