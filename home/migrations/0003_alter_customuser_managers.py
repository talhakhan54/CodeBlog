# Generated by Django 4.1.5 on 2023-02-28 05:32

import django.contrib.auth.models
from django.db import migrations
import home.manage


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customuser_address_customuser_bio_customuser_pic_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('object', home.manage.UserManager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
