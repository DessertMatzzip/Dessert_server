
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('user', views.join, name='join'),
    path('modify', views.modify, name='modify'),
]
