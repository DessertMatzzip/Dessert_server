# Generated by Django 2.0.7 on 2018-08-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_user_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='charField', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(default='charField', max_length=10),
        ),
    ]
