# Generated by Django 4.0.3 on 2022-04-15 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0002_alter_song_audio_file_alter_song_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalList',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_id', models.CharField(default='', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
