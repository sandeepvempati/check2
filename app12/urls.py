from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^hello/',views.hello,name='hello'),
    url(r'^index/',views.index,name='index')
]