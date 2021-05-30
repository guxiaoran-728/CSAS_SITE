from django.conf.urls import url
from django.urls import path

from . import views
from django.conf import settings
app_name = 'account'
urlpatterns = [
    path('', views.user_login),
    path('login', views.user_login),
    path('regist', views.register),


]
