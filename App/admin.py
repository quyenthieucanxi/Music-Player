from django.contrib import admin
from .models import Song
from .models import PersonalList,History
# Register your models here.
admin.site.register(Song)
admin.site.register(PersonalList)
admin.site.register(History)