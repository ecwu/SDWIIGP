from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group
from django.contrib import messages

from dashboard.models import MemberCard


def create_member(request):
    if not (request.user.is_superuser or request.user.is_staff):
        messages.add_message(request, messages.ERROR, 'No Permission.')
        return redirect('/')
    return render(request, 'create/member.html')


def create_coach(request):
    if not (request.user.is_superuser or request.user.is_staff):
        messages.add_message(request, messages.ERROR, 'No Permission.')
        return redirect('/')
    return render(request, 'create/coach.html')


def submit(request):
    if not (request.user.is_superuser or request.user.is_staff):
        messages.add_message(request, messages.ERROR, 'No Permission.')
        return redirect('/')
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')
    role = request.POST.get('role')

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )

    messages.add_message(request, messages.SUCCESS, 'The user has been created.')

    if role == 'member':
        new_membercard = MemberCard.objects.create(
            related_user=user
        )
        messages.add_message(request, messages.INFO, 'User\'s Member Card Number: ' + str(new_membercard.id) + '.')
    elif role == 'coach':
        coach_group = Group.objects.get(name='coach')
        user.groups.add(coach_group)
    return render(request, 'create/result.html', {'created': user, 'created_role': role})


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
