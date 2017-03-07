# -*-coding: utf-8 -*-

from django.conf.urls import url

from .views import userInfoView


urlpatterns = [
    # 用户信息
    url(r'^info/(?P<userNo>\d+)/$', userInfoView.as_view(), name='user_info'),
]