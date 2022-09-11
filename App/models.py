
from django.db import models
from django.contrib.auth.models import User
 

# Create your models here.
class Song(models.Model):
    #song_id=models.AutoField(primary_key=True)
    title = models.TextField()
    artist= models.TextField()
    image= models.ImageField(upload_to='images')
    audio_file = models.FileField(blank=True,null=True,upload_to='audio') 
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    category = models.TextField(blank=True,null=True)
    listens = models.TextField(blank=True,null=True,default=0)

    def __str__(self) :
        return self.title       
class PersonalList(models.Model):
    list_id= models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song_id= models.CharField(max_length=30,default="")
class History(models.Model):
    list_id= models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song_id= models.CharField(max_length=30,default="")