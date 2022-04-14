from django.shortcuts import render
from .models import Song
# Create your views here.
def index(request):
    song = Song.objects.all()
    return render(request,'index.html',{'song': song})
def songs(request):
    song = Song.objects.all()
    return render(request,'All_songs/songs.html',{'song': song})
def songpost(request,id):
    song= Song.objects.all()
    song_id=Song.objects.filter(pk=id).first()
    return render(request,'All_songs/songpost.html',{'song': song,'song_id': song_id})