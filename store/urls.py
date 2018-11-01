from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('call', views.callStore, name='callStore'),
    path('modify', views.modifyStore, name='modifyStore'),
    path('comment', views.commentStore, name='commentStore'),
    path('shutdown', views.shutdownStore, name='shutdownStore'),
    path('add', views.addStore, name='addStore'),
    path('select', views.selectRegion, name='selectRegion'),
]