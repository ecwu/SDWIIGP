from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateformat import format

from datetime import *

from .models import MemberCard, WorkoutRecord


def operation_checkin(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'operation/index.html')


def operation_recharge(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'operation/recharge.html')


def check_in_member(request):
    if not request.user.is_authenticated:
        return redirect('/')
    checkin_member_id = request.POST.get('member_id')
    checkin_member_object = MemberCard.objects.get(pk=checkin_member_id)
    if checkin_member_object.quota > 0:
        checkin_member_object.quota -= 1
        checkin_member_object.save()
        # Create Check in record
        WorkoutRecord.objects.create(
            related_member_card_id=checkin_member_object.id,
        )
    return redirect('/operation')


def pull_member_card_information(request):
    member_id = request.GET.get('memberID')
    member_card = MemberCard.objects.get(pk=member_id)
    member_card_owner_id = member_card.related_user_id
    member_card_owner = User.objects.get(pk=member_card_owner_id)
    date_join = datetime.fromtimestamp(int(format(member_card_owner.date_joined, "U")))
    member_join = (datetime.now()-date_join).days
    data = {
        'member_name_abbr': member_card_owner.first_name[0] + member_card_owner.last_name[0],
        'member_name': member_card_owner.first_name + " " + member_card_owner.last_name,
        'member_quota': member_card.quota,
        'member_join': member_join,
    }
    return JsonResponse(data)
