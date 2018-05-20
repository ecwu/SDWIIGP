from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def exist_appointment(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Login required.')
        return redirect('/')
    return render(request, 'appointment/appointment.html')


def new_appointment(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Login required.')
        return redirect('/')
    if request.user.groups.filter(name='coach').exists():
        messages.add_message(request, messages.ERROR, 'No Permission.')
        return redirect('/dashboard')
    Coach = User.objects.filter(groups__name='coach')
    return render(request, 'appointment/new.html', {'coach': Coach})
