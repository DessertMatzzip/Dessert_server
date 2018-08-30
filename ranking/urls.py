from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('reviewer/call', views.callRankingReviewer, name='callRankingReviewer'),
    path('store/call', views.callRankingStore, name='callRankingStore'),
]