from django.conf.urls import url, include
from django.contrib import admin
from bounty import views

urlpatterns = [
    url(r'^main/$', views.main, name='main'),
    url(r'^request_page/$', views.request_page, name='request_page'),
    url(r'^request/$', views.request, name='request'),
    url(r'^bounty_board_cus/$', views.bounty_board_cus, name='bounty_board_cus'),
    url(r'^bounty_board_del/$', views.bounty_board_del, name='bounty_board_del'),
    url(r'^(?P<quest_id>\d+)/detail_cus/$', views.detail_cus, name='detail_cus'),
    url(r'^(?P<quest_id>\d+)/detail_del/$', views.detail_del, name='detail_del'),
    url(r'^(?P<quest_id>\d+)/accept/$', views.accept, name='accept'),
    url(r'^(?P<quest_id>\d+)/modify_quest/$', views.modify_quest, name='modify_quest'),
    url(r'^(?P<quest_id>\d+)/delete_quest/$', views.delete_quest, name='delete_quest'),
    url(r'^(?P<quest_id>\d+)/progress_quest_cus/$', views.progress_quest_cus, name='progress_quest_cus'),
    url(r'^(?P<quest_id>\d+)/progress_quest_del/$', views.progress_quest_del, name='progress_quest_del'),
    url(r'^(?P<quest_id>\d+)/confirm_cus/$', views.confirm_cus, name='confirm_cus'),
    url(r'^(?P<quest_id>\d+)/confirm_del/$', views.confirm_del, name='confirm_del'),
    url(r'^(?P<quest_id>\d+)/confirm/$', views.confirm, name='confirm'),
    url(r'^(?P<quest_id>\d+)/cancel/$', views.cancel, name='cancel'),
    url(r'^(?P<quest_id>\d+)/complete_quest/$', views.complete_quest, name='complete_quest'),
]
