from django.urls import path
from django.conf.urls import url
from .views import register,login

urlpatterns=[
    path('register/',register),
    url(r'^login/$',login),
]
