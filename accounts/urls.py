from django.conf.urls import url, include
from django.contrib import admin
from accounts import views

urlpatterns = [
    url(r'^$', views.login_page, name='login_page'),
    url(r'^login/$', views.login, name='login',),
    url(r'^register_page/$', views.register_page, name='register_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^mypage/$', views.mypage, name="mypage"),
]
