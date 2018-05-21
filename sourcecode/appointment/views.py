from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .models import Appointment
from dashboard.models import MemberCard


def exist_appointment(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Login required.')
        return redirect('/')
    if request.user.is_staff or request.user.is_superuser:
        records = Appointment.objects.all()
    elif request.user.groups.filter(name='coach').exists():
        records = Appointment.objects.filter(appointee=request.user)
    else:
        user_membercard = MemberCard.objects.get(related_user=request.user)
        records = Appointment.objects.filter(appointer=user_membercard)
    return render(request, 'appointment/appointment.html', {'records': records})


def new_appointment(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Login required.')
        return redirect('/')
    if request.user.groups.filter(name='coach').exists():
        messages.add_message(request, messages.ERROR, 'No Permission.')
        return redirect('/dashboard')
    if request.user.is_authenticated and request.user.is_staff:
        messages.add_message(request, messages.WARNING,
                             'This account have no Member Card . You cannot make appointments.')
    Coach = User.objects.filter(groups__name='coach')
    try:
        usermembercard = MemberCard.objects.get(related_user=request.user)
    except ObjectDoesNotExist:
        usermembercard = None
    return render(request, 'appointment/new.html', {'coach': Coach, 'usermembercard': usermembercard})


def check_coach_time(request):
    if request.user.is_authenticated:
        coach_name = request.GET.get('coach_name')
        select_date = request.GET.get('select_date')
        select_hour = request.GET.get('select_hour')
    pass

