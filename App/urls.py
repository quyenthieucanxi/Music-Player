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
    path('Login/logout/',views.logout,name='logout'),
    path('Login/signup/',views.signup,name='signup'),
    path('Login/PersonalList/',views.personallist,name='personallist'),
    path('Login/History/',views.history,name='history'),
    path('All_songs/search/',views.search,name='search'),
    path('All_songs/albumViet/',views.albumViet,name='albumViet'),
    path('All_songs/albumKorea/',views.albumKorea,name='albumKorea'),
    path('All_songs/albumUK/',views.albumUK,name='albumUK'),
    path('All_songs/album/',views.albums,name='albums'),
    path('Login/album/',views.Albums,name='Albums'),
    path('Login/albumViet/',views.AlbumViet,name='AlbumViet'),
    path('Login/albumKorea/',views.AlbumKorea,name='AlbumKorea'),
    path('Login/albumUK/',views.AlbumUK,name='AlbumUK'),
    path('Login/search/',views.LoginSearch,name='LoginSearch'),
    path('Login/upload/', views.Upload, name = 'upload')

]