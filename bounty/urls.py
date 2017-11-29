from django.conf.urls import url, include
from django.contrib import admin
from bounty import views

urlpatterns = [
    url(r'^main/$', views.main, name='main'),
    url(r'^profile_req/$', views.profile_req, name='profile_req'),
    url(r'^profile_ful/$', views.profile_ful, name='profile_ful'),
    url(r'^request/$', views.request, name='request'),
    url(r'^ongoing/$', views.ongoing, name='ongoing'),
    url(r'^bounty_board/$', views.bounty_board, name='bounty_board'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^progress/$', views.progress, name='progress'),
    url(r'^confirm_cus/$', views.confirm_cus, name='confirm_cus'),
    url(r'^confirm_del/$', views.confirm_del, name='confirm_del'),
]
