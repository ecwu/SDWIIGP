from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def exist_appointment(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'appointment/appointment.html')


def new_appointment(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'appointment/new.html')