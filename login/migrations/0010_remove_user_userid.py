# Generated by Django 2.0.7 on 2018-09-05 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userid',
        ),
    ]
