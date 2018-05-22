from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from . import models

from dashboard.models import MemberCard
from operation.models import WorkoutRecord, RechargeLog
from appointment.models import Appointment


def report(request):
    if not (request.user.is_authenticated and request.user.is_staff):
        messages.add_message(request, messages.ERROR, 'No Permission.')
        return redirect('/')
    Member = MemberCard.objects.all()
    Coach = User.objects.filter(groups__name='coach')
    Workout = WorkoutRecord.objects.all()
    Recharge = RechargeLog.objects.all()
    Recharge_waiting = RechargeLog.objects.filter(is_valid=False)
    Appointments = Appointment.objects.all()
    Recharge_balance = 0
    for recharge_payment in Recharge:
        Recharge_balance += int(recharge_payment.quota) * 20
    Today_recharge_balance = 0
    for recharge_payment in Recharge_waiting:
        Today_recharge_balance += int(recharge_payment.quota) * 20
    return render(request, 'report/index.html', {'member': Member,
                                                 'coach': Coach,
                                                 'workout': Workout,
                                                 'recharge': Recharge,
                                                 'w_recharge': Recharge_waiting,
                                                 'balance': Recharge_balance,
                                                 'appointment': Appointments,
                                                 'waiting': Today_recharge_balance})
