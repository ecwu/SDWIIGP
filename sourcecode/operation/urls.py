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
    path('operation/', views.operation_checkin, name="operation_checkin"),
    path('operation/recharge/', views.operation_recharge, name="operation_recharge"),
    path('operation/recharge/submit/', views.get_recharge, name="getrecharge"),
    path('operation/recharge/invoke/<int:recharge_id>', views.recharge_invoke, name="invoke_recharge"),
    path('operation/recharge/accept/<int:recharge_id>', views.recharge_accept, name="accept_recharge"),
    path('operation/member-info/', views.pull_member_card_information, name="pull_info"),
    path('operation/member-check/', views.check_in_member, name="checkin_member")
]
