"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#
# @author huangpingyi
# coding:utf-8

from django.conf.urls import include, url
from webqq import views


urlpatterns = [
   url(r'^/$', views.dashboard, name='chat'),
   url(r'^send_msg/$', views.send_msg, name='chat_send_msg'),
    url(r'^get_msg/$', views.get_msg, name='get_new_msg'),
]
