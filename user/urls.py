from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('call/review', views.callReview, name='callReview'),
    path('call/snshome', views.callSnsHome, name='callSnsHome'),
    path('follow/call', views.callFollow, name='callFollow'),
    path('follower/call', views.callFollower, name='callFollower'),
    path('collection/call', views.callCollection, name='callCollection'),
    path('collection/delete', views.deleteCollection, name='deleteCollection'),
    path('collection/create', views.createCollection, name='createCollection'),
    path('collection/list/call', views.callCollectionList, name='callCollectionList'),
    path('collection/list/add', views.addCollectionList, name='addCollectionList'),
    path('collection/list/delete', views.deleteCollectionList, name='deleteCollectionList'),
    path('store/call', views.callStoreList, name='callStoreList'),
    path('store/storage', views.storageStoreList, name='storageStoreList'),
    path('store/delete', views.deleteStoreList, name='deleteStoreList'),
]