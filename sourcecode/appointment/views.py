from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
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
        records = Appointment.objects.all()[:100]
    elif request.user.groups.filter(name='coach').exists():
        records = Appointment.objects.filter(appointee=request.user)[:10]
    else:
        user_membercard = MemberCard.objects.get(related_user=request.user)
        records = Appointment.objects.filter(appointer=user_membercard)[:10]
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
        available_time = True
        coach_object = User.objects.get(pk=coach_name)
        if Appointment.objects.filter(appointee=coach_object, appoint_time_date=select_date,
                                      appoint_time_hour=select_hour).exists():
            available_time = False
        data = {
            'available_time': available_time,
            'coach_name': coach_name,
            'select_date': select_date,
            'select_hour': select_hour,
        }
        return JsonResponse(data)


def make_new_appointment(request):
    if request.user.is_authenticated:
        coach_name = request.POST.get('coach_name')
        select_date = request.POST.get('select_date')
        select_hour = request.POST.get('select_hour')
        coach_object = User.objects.get(pk=coach_name)
        request_user_membercard = MemberCard.objects.get(related_user=request.user)
        Appointment.objects.create(
            appointer=request_user_membercard,
            appointee=coach_object,
            appoint_time_date=select_date,
            appoint_time_hour=select_hour,
        )
        messages.add_message(request, messages.SUCCESS, 'Appoint Successfully!')
        return redirect('/appointment')
