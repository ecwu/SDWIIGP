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

def submit(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'create/result.html')

def check_username(request):
    username = request.GET.get('username')
    data = {
        'is_taken': User.objects.filter(username__exact=username).exists()
    }
    return JsonResponse(data)

def check_email(request):
    email = request.GET.get('email')
    data = {
        'is_taken': User.objects.filter(email__exact=email).exists()
    }
    return JsonResponse(data)
