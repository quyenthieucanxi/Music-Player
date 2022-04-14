from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('All_songs/songs/',views.songs,name='songs'),
    path('All_songs/songs/<int:id>',views.songpost,name='songpost'),
]