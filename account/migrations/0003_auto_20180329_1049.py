# Generated by Django 2.0.2 on 2018-03-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pic',
            field=models.ImageField(blank=True, upload_to='profile'),
        ),
    ]
