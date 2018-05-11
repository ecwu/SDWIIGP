from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def create_member(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'create/member.html')


def create_coach(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'create/coach.html')


def result(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'create/result.html')


def user_name_check(request):
    pass
