
from email.headerregistry import Address
from django.shortcuts import render
from matplotlib.pyplot import title
from .models import Song, PersonalList,History
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.shortcuts import redirect
from django.core.mail import *


# Create your views here.
def index(request):
    songs = Song.objects.filter(listens__gte = 50)
    return render(request,'index.html',{'song': songs})
def home(request):
    song = Song.objects.filter(listens__gte = 50)
    return render(request,'Login/home.html',{'song': song})

def songs(request):
    #song = Song.objects.all()
    song = Song.objects.all().order_by('title')
    return render(request,'All_songs/songs.html',{'song': song})
def login_songs(request):
    #song = Song.objects.all()
    song = Song.objects.all().order_by('title')
    return render(request,'Login/songs.html',{'song': song})
def login_songpost(request,id):
    song= Song.objects.all()
    song_id=Song.objects.filter(pk=id).first()
    listens = int(song_id.listens) + 1
    song_id.listens = listens
    song_id.save()
    return render(request,'Login/songpost.html',{'song': song,'song_id': song_id})
def songpost(request,id):
    song= Song.objects.all()
    song_id=Song.objects.filter(pk=id).first()
    listens = int(song_id.listens) + 1
    song_id.listens = listens
    song_id.save()
    
    return render(request,'All_songs/songpost.html',{'song': song,'song_id': song_id})
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username= username,password=password)
        from django.contrib.auth import login
        if user and user.is_active:
            login(request, user)
            return redirect('/Login/login/home/')
        else:   
            return render(request,'Login/loginagain.html')
    return render(request,'Login/login.html')
def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')

def signup(request):
    error_message = None
    if request.method == "POST":
        email= request.POST['email']
        username= request.POST['username']
        first_name= request.POST['firstname']
        last_name = request.POST['lastname']
        pass_1=request.POST['pass1']
        pass_2 = request.POST['pass2']
        
        def isExistsEmail(email):
            if User.objects.filter(email=email):
                return True
            return False
        def isExistsUsername(username):
            if User.objects.filter(username=username):
                return True
            return False
        if not first_name:
            error_message = "Vui lòng nhập First Name"
        elif not last_name:
            error_message = "Vui lòng nhập Last Name"
        elif not pass_1:
            error_message = "Vui lòng nhập Password"
        elif not pass_2 or pass_1 != pass_2:
            error_message = "Mật khẩu nhập lại không chính xác"
        elif isExistsEmail(email):
            error_message = "Địa chỉ email đã được đăng ký"
        elif isExistsUsername(username):
            error_message = "Username đã được đăng ký"
        else:
            myuser=User.objects.create_user(username,email,pass_1)
            myuser.first_name= first_name
            myuser.last_name = last_name
            myuser.save()
            error_message = "Đăng kí thành công"
            message = "Cảm ơn bạn đã đăng ký!"
            subject = "Welcom"
            send_mail(
            subject,
            message,
            'congquyenhuynh111@gmail.com',
            [email],
            fail_silently=False,
        )
            return render(request,'Login/signup.html',{"error_message":error_message,'send_mail':send_mail})
    return render(request,'Login/signup.html',{"error_message":error_message})

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
def history(request):
    if request.method == "POST":
        user = request.user
        song_id =request.POST['song_id']
        history_list= History(user= user,song_id= song_id)
        history_list.save()
        return redirect(f'/Login/songs/{song_id}',{'song_id':song_id})
    history_List= History.objects.filter(user=request.user)
    listSong= []
    for i in history_List:
        listSong.append(i.song_id)
    song = Song.objects.filter(id__in=listSong)    
    return render(request,"Login/history.html",{'song':song})
def search(request):
    query = request.GET.get("query")
    song = Song.objects.all()
    qs= song.filter(title__icontains=query)|song.filter(artist__icontains=query)
    #qs1= song.filter(artist__icontains=query)
    
    return render(request,"All_songs/search.html",{"song": qs})
def LoginSearch(request):
    query = request.GET.get("query")
    song = Song.objects.all()
    qs= song.filter(title__icontains=query)|song.filter(artist__icontains=query)
    return render(request,"Login/search.html",{"song": qs})
def albumViet(request):
    song = Song.objects.filter(category='VPOP')
    return render(request,"All_songs/album.html",{'song':song})
def albumKorea(request):
    song = Song.objects.filter(category='KPOP')
    return render(request,"All_songs/album.html",{'song':song})
def albumUK(request):
    song = Song.objects.filter(category='UK')
    return render(request,"All_songs/album.html",{'song':song})  
def albums(request):
    return render(request,"All_songs/albums.html")
def Albums(request):
    return render(request,"Login/albums.html")  
def AlbumViet(request):
    song = Song.objects.filter(category='VPOP')
    return render(request,"Login/album.html",{'song':song})
def AlbumKorea(request):
    song = Song.objects.filter(category='KPOP')
    return render(request,"Login/album.html",{'song':song})
def AlbumUK(request):
    song = Song.objects.filter(category='UK')
    return render(request,"Login/album.html",{'song':song}) 

def Upload(request):
    if request.method == "POST":
        songname = request.POST['songname']
        artistname = request.POST['artistname']
        category = request.POST['category']
        audio_link = request.POST['audio_link']
        user= request.user
        email= user.email
        message = str({'Mail':email , 'Song name: ': songname, ' Artistname: ': artistname, 'Category: ': category, ' Audio_link: ': audio_link})
        subject = "Request Upload"
        mail_admins(
            subject,
            message,
            fail_silently=False,)
        send= 'Send Success'
        return render(request,"Login/upload.html", {'send': send})
    return render(request,"Login/upload.html")
