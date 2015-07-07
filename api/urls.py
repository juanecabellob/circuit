"""@package api
Url patterns for API

@author 7Pros
@copyright 
"""
from django.conf.urls import url
from .views import user_login, post_create, RootView

urlpatterns = [
    url(r'^$', RootView.as_view(), name='api_root'),
    url(r'^login/$', user_login, name='login'),
    url(r'^post-create/$', post_create, name='post-create'),
]