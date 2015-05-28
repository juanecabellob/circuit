from django.conf.urls import url
from users import views
from users.views import (
    UserCreateView,
    UserCreateConfirmView,
    # UserLoginView,
    # UserLogoutView,
    UserProfileView,
    # UserUpdateView,
    # UserDeleteView,
)

urlpatterns = [
    url(r'^signup/$', UserCreateView.as_view(), name='signup'),
    url(r'^signup/confirm/(?P<token>\w+)/$', views.UserCreateConfirmView, name='signup_confirm'),
    # url(r'^login/$', UserLoginView.as_view(), name='login'),
    # url(r'^login/$', UserLogoutView.as_view(), name='logout'),
    url(r'^(?P<pk>\d+)/$', UserProfileView.as_view(), name='profile'),
    # url(r'^(?P<pk>\d+)/edit/$', UserUpdateView.as_view(), name='edit'),
    # url(r'^(?P<pk>\d+)/delete/$', UserDeleteView.as_view(), name='delete'),
]
