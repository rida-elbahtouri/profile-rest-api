# Generated by Django 3.0.2 on 2020-02-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='name', max_length=255),
        ),
    ]
