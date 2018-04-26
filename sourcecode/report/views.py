from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from . import models


def report(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'report/index.html')