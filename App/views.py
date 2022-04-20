import email
from django.shortcuts import render
from .models import Song, PersonalList
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.db.models import Case,When
# Create your views here.
def index(request):
    song = Song.objects.all()
    return render(request,'index.html',{'song': song})
def home(request):
    song = Song.objects.all()
    return render(request,'Login/home.html',{'song': song})
def songs(request):
    song = Song.objects.all()
    return render(request,'All_songs/songs.html',{'song': song})
def login_songs(request):
    song = Song.objects.all()
    return render(request,'Login/songs.html',{'song': song})
def login_songpost(request,id):
    song= Song.objects.all()
    song_id=Song.objects.filter(pk=id).first()
    return render(request,'Login/songpost.html',{'song': song,'song_id': song_id})
def songpost(request,id):
    song= Song.objects.all()
    song_id=Song.objects.filter(pk=id).first()
    '''if request.method == "POST":
        message = 'You need to login'
        return redirect(request,f'/All_songs/songs/{{song_id.id}}',{'song': song,'song_id': song_id,'message':message})
    else:
        message= ""'''
    return render(request,'All_songs/songpost.html',{'song': song,'song_id': song_id})
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username= username,password=password)
        from django.contrib.auth import login
        login(request, user)
        if user is not None:
            return redirect('/Login/login/home/')
        else:
            return render(request,'Login/loginagain.html')
    return render(request,'Login/login.html')
def signup(request):
    if request.method == "POST":
        email= request.POST['email']
        username= request.POST['username']
        first_name= request.POST['firstname']
        last_name = request.POST['lastname']
        pass_1=request.POST['pass1']
        pass_2 = request.POST['pass2']
        
        myuser=User.objects.create_user(username,email,pass_1)
        myuser.first_name= first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username= username,password=pass_1)
        from django.contrib.auth import login
        login(request, user)
        return redirect('/')
    return render(request,'Login/signup.html')
def personallist(request):
    if request.method == "POST":
        user = request.user
        song_id =request.POST['song_id']
        personal_list= PersonalList.objects.filter(user=user)
        for i in personal_list:
            if song_id == i.song_id:
                messages = "Your Song is Already Added"
                break
        else:   
            personallist= PersonalList(user= user,song_id= song_id)
            personallist.save()
            messages = "Your Song is Succesfully Added"
        
        song_id=Song.objects.filter(id=song_id).first()
        #song= Song.objects.all()
        return render(request,"Login/songpost.html",{'messages': messages,'song_id':song_id})       
        #return redirect(f'/Login/songs/{song}',{'song_id':song_id,'messages':messages})
    personal_list= PersonalList.objects.filter(user=request.user)
    listSong= []
    for i in personal_list:
        listSong.append(i.song_id)
    #preserved = Case(*[When(pk=pk,then=pos)for pos,pk in enumerate(listSong)])
    song = Song.objects.filter(id__in=listSong)
    return render(request,'Login/personallist.html',{'song':song})
