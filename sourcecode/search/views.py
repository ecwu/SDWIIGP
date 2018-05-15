from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from dashboard.models import MemberCard


def search(request):
    if not request.user.is_authenticated:
        return redirect('/')
    number_query_user = None
    search_key = None
    number_member_card = None
    string_query_user = None
    if request.method == 'GET' and 'search_key' in request.GET:
        search_key = request.GET.get('search_key')
        try:
            number_member_card = MemberCard.objects.filter(pk=search_key)
            number_query_user = User.objects.filter(pk=search_key)
        except ValueError:
            pass
        string_query_user = User.objects.filter(username__contains=search_key)

    return render(request, 'search/index.html', {'number_query_user' : number_query_user, 'search_key': search_key, 'member_card_owner': number_member_card, 'string_query_user': string_query_user})