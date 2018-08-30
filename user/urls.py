from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('follow/call', views.callFollow, name='callFollow'),
    path('follower/call', views.callFollower, name='callFollower'),
    path('collection/call', views.callCollection, name='callCollection'),
    path('collection/storage', views.storageCollection, name='storageCollection'),
    path('store/call', views.callStoreList, name='callStoreList'),
    path('store/storage', views.storageStoreList, name='storageStoreList'),
]