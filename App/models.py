from distutils.command.upload import upload
from msilib.schema import Class
from django.db import models

# Create your models here.
class Song(models.Model):
    #song_id=models.AutoField(primary_key=True)
    title = models.TextField()
    artist= models.TextField()
    image= models.ImageField(upload_to='images')
    audio_file = models.FileField(blank=True,null=True,upload_to='audio') 
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    def __str__(self) :
        return self.title       