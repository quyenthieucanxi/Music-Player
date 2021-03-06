# Generated by Django 4.0.3 on 2022-04-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
