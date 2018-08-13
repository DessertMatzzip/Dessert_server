
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('facebook', views.loginFacebook, name='loginFacebook'),
    path('kakao', views.loginKakao, name='loginKakao'),
    path('itself', views.loginItself, name='loginItself'),
]
