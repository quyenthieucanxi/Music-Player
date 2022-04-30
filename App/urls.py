from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('Login/login/home/',views.home,name='home'),
    path('All_songs/songs/',views.songs,name='songs'),
    path('All_songs/songs/<int:id>',views.songpost,name='songpost'),
    path('Login/songs/',views.login_songs,name='login_songs'),
    path('Login/songs/<int:id>',views.login_songpost,name='login_songpost'),
    path('Login/login/',views.login,name='login'),
    path('Login/signup/',views.signup,name='signup'),
    path('Login/PersonalList/',views.personallist,name='personallist'),
    path('Login/History/',views.history,name='history'),

]