
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('itself', views.joinItself, name='joinItself'),
    path('kakao', views.joinKakao, name='joinKakao'),
    path('facebook', views.joinFacebook, name='joinFacebook'),
    path('modify', views.modify, name='modify'),
]
