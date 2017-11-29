from django.shortcuts import render
from bounty.models import User, Quest
# Create your views here.


def login_page(request):

    return render(request, 'accounts/login_page.html', )

# def login(request):
#     return render(request, '')

def register_page(request):
    return render(request, 'accounts/register_page.html', )


def register(request):
    return render(request, 'accounts/login_page.html', )


def mypage(request):

    return render(request, 'accounts/mypage.html', )