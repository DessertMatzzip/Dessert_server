# Generated by Django 2.0.7 on 2018-12-26 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_user_introduce'),
        ('user', '0004_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='userid',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
    ]
