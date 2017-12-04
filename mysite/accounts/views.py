import json

from django.shortcuts import render, redirect
from bounty.models import Quest
from accounts.forms import RegistrationForm, AuthenticationForm
from django.contrib.auth import login as login_auth, logout as logout_auth, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.


def login_page(request):

    return render(request, 'accounts/login_page.html', )

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            tmp_email = request.POST.get('email')
            tmp_password = request.POST.get('password')

            user = authenticate(username=tmp_email, password=tmp_password)

            if user is not None:
                login_auth(request, user)
                data = {'status': 'success', 'message': "login success."}
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                data = {'status': 'fail', 'message': "Id and password do not match. please check again."}
                return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return render(request, 'accounts/login.html', {})


def logout(request):
    logout_auth(request)
    return redirect('/')


def register_page(request):
    return render(request, 'accounts/register_page.html', )


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            tmp_username = request.POST.get('username')
            tmp_email = request.POST.get('email')
            tmp_password1 = request.POST.get('password1')
            tmp_password2 = request.POST.get('password2')

            if tmp_password1 != tmp_password2:
                response = {'status':'fail', 'message': "Password and password verification do not match. Please check again."}
                return HttpResponse(json.dumps(response), content_type='application/json')
            elif tmp_email.find(".") == -1:
                response = {'status':'fail', 'message': "Inappropriate email address. Please enter a valid email address."}
                return HttpResponse(json.dumps(response), content_type='application/json')
            elif User.objects.filter(username=tmp_username).exists():
                response = {'status':'fail', 'message': "This username already exists. Please enter another username."}
                return HttpResponse(json.dumps(response), content_type='application/json')
            elif User.objects.filter(email=tmp_email).exists():
                response = {'status':'fail', 'message': "This email already exists. Please enter another email."}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                user = User.objects.create_user(
                    username=tmp_username,
                    password=tmp_password1,
                    email=tmp_email
                )

                response = {'status': 'success', 'message': "Welcome!!"}
                return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return redirect('login_page')


def mypage(request):
    quest_li_waiting = list()
    quest_li_ongoing_cus = list()
    quest_li_ongoing_del = list()
    quest_li_complete_cus = list()
    quest_li_complete_del = list()
    requested = 0
    fulfilled = 0
    user = request.user

    for quest in Quest.objects.all().order_by('-create_date'):
        if quest.status == 'ongoing':
            if request.user.username == quest.customer:
                quest_li_ongoing_cus.append(quest)

            elif request.user.username == quest.deliver:
                quest_li_ongoing_del.append(quest)

        elif quest.status == 'complete':
            if request.user.username == quest.customer:
                requested += 1
                quest_li_complete_cus.append(quest)

            elif request.user.username == quest.deliver:
                fulfilled += 1
                quest_li_complete_del.append(quest)

        elif quest.status == 'waiting':
            quest_li_waiting.append(quest)

    context = {
        'quest_waiting': quest_li_waiting,
        'quest_ongoing_cus': quest_li_ongoing_cus,
        'quest_ongoing_del': quest_li_ongoing_del,
        'quest_complete_cus': quest_li_complete_cus,
        'quest_complete_del': quest_li_complete_del,
        'requested':requested,
        'fulfilled':fulfilled,
        'user':user,
    }

    return render(request, 'accounts/mypage.html', context)
