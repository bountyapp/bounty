import json

from django.shortcuts import render, redirect, get_object_or_404
from bounty.models import Quest
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages


import datetime
# Create your views here.


def main(request):
    return render(request, 'bounty/main.html', )


def bounty_board_cus(request):

    if not request.user.is_authenticated():
        messages.success(request, "You have to login for this service.")
        return render(request, 'accounts/login_page.html', {})

    quest_list_waiting = list()
    quest_list_ongoing = list()
    quest_list_complete = list()

    for quest_item in Quest.objects.filter(customer=request.user.username).order_by('-create_date'):
        if quest_item.status == 'waiting':
            quest_list_waiting.append(quest_item)
        elif quest_item.status == 'ongoing':
            quest_list_ongoing.append(quest_item)
        elif quest_item.status == 'complete':
            quest_list_complete.append(quest_item)

    context = {
        'quest_waiting':quest_list_waiting,
        'quest_ongoing':quest_list_ongoing,
        'quest_complete':quest_list_complete
    }
    return render(request, 'bounty/bounty_board_cus.html', context)


def request_page(request):
    return render(request, 'bounty/request_page.html', )


def request(request):
    if request.method == 'POST':
        tmp_customer = request.user.username
        tmp_contents = request.POST.get('contents')
        tmp_places = request.POST.get('places')
        tmp_destination = request.POST.get('destination')
        tmp_due = request.POST.get('due')
        tmp_cost = float(request.POST.get('cost'))
        tmp_reward = float(request.POST.get('reward'))
        tmp_total = tmp_reward-tmp_cost
        tmp_comments = request.POST.get('comments')

        if tmp_contents == '-':
            response = {'status': 'fail', 'message': "You have to write the contents."}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif tmp_places == '-':
            response = {'status': 'fail', 'message': "You have to write the places."}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif tmp_destination== '-':
            response = {'status': 'fail', 'message': "You have to write the destination."}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif tmp_due == None:
            response = {'status': 'fail', 'message': "You have to write the due."}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif tmp_cost== '-':
            response = {'status': 'fail', 'message': "You have to write the cost."}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif tmp_reward== '-':
            response = {'status': 'fail', 'message': "You have to write the reward."}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif int(tmp_cost) > int(tmp_reward):
            response = {'status': 'fail', 'message': "reward have to be higher than cost."}
            return HttpResponse(json.dump(response), content_type='application/json')
        else:
            Quest.objects.create(customer=tmp_customer,
                                 contents=tmp_contents,
                                 places=tmp_places,
                                 destination=tmp_destination,
                                 due=tmp_due,
                                 cost=tmp_cost,
                                 reward=tmp_reward,
                                 total=tmp_total,
                                 comments=tmp_comments,
                                 )
            response = {'status': 'success', 'message': "Posting!"}
            return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        return redirect('bounty:request_page')



def detail_cus(request, quest_id):
    quest = get_object_or_404(Quest, pk=quest_id)

    return render(request, 'bounty/detail_cus.html', {'quest':quest})


def modify_quest(request, quest_id):
    q= Quest.objects.get(pk=quest_id)

    q.contents = request.POST.get('contents')
    q.places = request.POST.get('places')
    q.destination = request.POST.get('destination')
    q.due = request.POST.get('due')
    q.cost = float(request.POST.get('cost'))
    q.reward = float(request.POST.get('reward'))
    q.total = q.reward - q.cost
    q.comments = request.POST.get('comments')
    q.save()

    return redirect('bounty:bounty_board_cus')


def delete_quest(request, quest_id):
    Quest.objects.filter(pk=quest_id).delete()

    return redirect('bounty:bounty_board_cus')


def progress_quest_cus(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)

    return render(request, 'bounty/progress_quest_cus.html', {'quest':quest})


def confirm_cus(request, quest_id):
    quest= Quest.objects.get(pk=quest_id)

    return render(request, 'bounty/confirm_cus.html', {'quest':quest})


def confirm(request, quest_id):

    q = Quest.objects.get(pk=quest_id)

    if request.user.username == q.customer:
        q.score_cus = request.POST.get('score_cus')
        q.review_cus = request.POST.get('review_cus')
        q.confirm_cus = True
        q.save()

    if request.user.username == q.deliver:
        q.score_del = request.POST.get('score_del')
        q.review_del = request.POST.get('review_del')
        q.confirm_del = True
        q.save()

    if q.confirm_cus == True and q.confirm_del == True:
        # 이체 완료 후
        q.status = 'complete'
        q.complete_date = datetime.datetime.now()
        q.save()

        response = {'status': 'success',
                    'message': "Thank you!! bounty is completed."}

    elif q.confirm_cus == True and q.confirm_del == False:
        response = {'status': 'success',
                    'message': "Thank you!! after confirm of deliver, bounty will be completed"}

    elif q.confirm_cus == False and q.confirm_del == True:
        response = {'status': 'success',
                    'message': "Thank you!! after confirm of customer, bounty will be completed"}

    return HttpResponse(json.dumps(response), content_type='application/json')

def bounty_board_del(request):
    quest_list = list()

    for quest_item in Quest.objects.filter(status='waiting'):
        quest_list.append(quest_item)

    context = {
        'quest_list': quest_list,
    }
    return render(request, 'bounty/bounty_board_del.html', context)


def detail_del(request, quest_id):
    if not request.user.is_authenticated():
        messages.success(request, "You have to login for this service.")
        return render(request, 'accounts/login_page.html', {})

    quest = get_object_or_404(Quest, pk= quest_id)

    if request.user.username == quest.customer:
        return render(request, 'bounty/detail_cus.html', {'quest':quest})

    return render(request, 'bounty/detail_del.html', {'quest':quest})


def accept(request, quest_id):
    q = Quest.objects.get(pk=quest_id)

    if q.status == 'ongoing' or q.status == 'complete':
        # messages.success(request, "Bounty is canceled or ongoing..")
        # return redirect('bounty:progress_quest_del', quest_id)

        response = {'status': 'fail', 'message': "Bounty was canceled."}
        return HttpResponse(json.dumps(response), content_type='application/json')

    q.status = 'ongoing'
    q.deliver = request.user.username
    q.save()

    # messages.success(request, "Bounty will be started.")
    # return redirect('bounty:progress_quest_del', quest_id)

    response = {'status': 'success', 'message': "Bounty will be started."}
    return HttpResponse(json.dumps(response), content_type='application/json')

def progress_quest_del(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)

    return render(request, 'bounty/progress_quest_del.html', {'quest':quest})


def confirm_del(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)

    return render(request, 'bounty/confirm_del.html', {'quest':quest})


def cancel(request, quest_id):
    q = Quest.objects.get(pk=quest_id)

    if request.user.username == q.customer:
        q.status = 'canceled'
        q.canceled_reason_cus = request.POST.get('reason')
        q.save()

    elif request.user.username == q.deliver:
        q.status = 'waiting'
        q.canceled_reason_del = request.POST.get('reason')
        q.save()

    response = {'status': 'success', 'message': "Bounty is canceled"}
    return HttpResponse(json.dumps(response), content_type='application/json')


def complete_quest(request, quest_id):
    quest = Quest.objects.get(pk=quest_id)

    return render(request, 'bounty/complete_quest.html', {'quest':quest})