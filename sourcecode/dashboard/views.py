from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from . import models

from operation.models import WorkoutRecord
# Create your views here.


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'dashboard/index.html')


def user_info(request):
    if not request.user.is_authenticated:
        return redirect('/')
    try:
        user_membercard = models.MemberCard.objects.get(related_user_id=request.user.id)
    except ObjectDoesNotExist:
        user_membercard = None
    try:
        user_workout = WorkoutRecord.objects.filter(related_member_card_id=user_membercard.id)
    except (ObjectDoesNotExist, AttributeError):
        user_workout = None
    return render(request, 'dashboard/user.html', {'user_membercard': user_membercard,
                                                   'user_workout_records': user_workout})
