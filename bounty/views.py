from django.shortcuts import render
from bounty.models import User, Quest
# Create your views here.


def main(request):
    return render(request, 'bounty/main.html', )


def profile_req(request):
    return render(request, 'bounty/profile_req.html', )


def profile_ful(request):
    return render(request, 'bounty/profile_ful.html', )


def ongoing(request):
    return render(request, 'bounty/ongoing.html', )


def request(request):
    return render(request, 'bounty/request.html', )


def bounty_board(request):
    return render(request, 'bounty/bounty_board.html',)


def detail(request):
    return render(request, 'bounty/detail.html', )


def progress(request):
    return render(request, 'bounty/progress.html', )


def confirm_cus(request):
    return render(request, 'bounty/confirm_cus.html')

def confirm_del(request):
    return render(request, 'bounty/confirm_del.html')