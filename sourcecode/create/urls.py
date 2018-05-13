"""gms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('create/member/', views.create_member, name="create_member"),
    path('create/coach/', views.create_coach, name="create_coach"),
    path('create/submit/', views.submit, name="create_submit"),
    path('create/check/username', views.check_username, name="check_username"),
    path('create/check/email', views.check_email, name="check_email"),
]
