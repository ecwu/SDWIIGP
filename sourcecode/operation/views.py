from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateformat import format
from django.contrib import messages

from datetime import *

from .models import MemberCard, WorkoutRecord, RechargeLog


def operation_checkin(request):
    if not (request.user.is_superuser or request.user.is_staff):
        messages.add_message(request, messages.ERROR, 'No Permission.')
        return redirect('/')
    return render(request, 'operation/index.html')


def operation_recharge(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Login required.')
    if request.user.groups.filter(name='coach').exists():
        messages.add_message(request, messages.ERROR, 'No Permission.')
        return redirect('/')
    padding_request = RechargeLog.objects.filter(is_valid=False)[:10]
    return render(request, 'operation/recharge.html', {'PaddingRequest': padding_request})


def get_recharge(request):
    if not request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Login required.')
        return redirect('/')
    recharge_card = request.POST.get('member_id')
    recharge_quota = request.POST.get('recharge_quota')
    recharge_method = request.POST.get('method')
    membercard_object = MemberCard.objects.get(pk=recharge_card)
    if recharge_method == "wechat":
        db_method = "WECHATPAY"
    else:
        db_method = "ALIPAY"

    recharge_log = RechargeLog.objects.create(
        related_member_card=membercard_object,
        quota=recharge_quota,
        recharge_method=db_method
    )
    messages.add_message(request, messages.SUCCESS, 'Payment No.' + str(recharge_log.id) + ' created.')
    return redirect('/operation/recharge')


def recharge_invoke(request, recharge_id):
    if not (request.user.is_superuser or request.user.is_staff):
        messages.add_message(request, messages.ERROR, 'No Permission.')
        return redirect('/')
    RechargeLog.objects.filter(pk=recharge_id).delete()
    messages.add_message(request, messages.SUCCESS, 'Payment deleted.')
    return redirect('/operation/recharge/')


def recharge_accept(request, recharge_id):
    if not (request.user.is_superuser or request.user.is_staff):
        messages.add_message(request, messages.ERROR, 'No Permission.')
        return redirect('/')
    recharge = RechargeLog.objects.get(pk=recharge_id)
    quota = recharge.quota

    recharge.related_member_card.quota += quota
    recharge.related_member_card.save()

    recharge.is_valid = True
    recharge.save()
    messages.add_message(request, messages.SUCCESS, 'Payment accepted.')
    return redirect('/operation/recharge/')


def check_in_member(request):
    if not (request.user.is_superuser or request.user.is_staff):
        messages.add_message(request, messages.ERROR, 'No Permission.')
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
        messages.add_message(request, messages.SUCCESS,
                             'Check in success! Left Quota: ' + str(checkin_member_object.quota))
    else:
        messages.add_message(request, messages.ERROR, 'No enough quota.')

    return redirect('/operation')


def pull_member_card_information(request):
    member_id = request.GET.get('memberID')
    member_card = MemberCard.objects.get(pk=member_id)
    member_card_owner_id = member_card.related_user_id
    member_card_owner = User.objects.get(pk=member_card_owner_id)
    date_join = datetime.fromtimestamp(int(format(member_card_owner.date_joined, "U")))
    member_join = (datetime.now() - date_join).days
    data = {
        'member_name_abbr': member_card_owner.first_name[0] + member_card_owner.last_name[0],
        'member_name': member_card_owner.first_name + " " + member_card_owner.last_name,
        'member_quota': member_card.quota,
        'member_join': member_join,
    }
    return JsonResponse(data)
