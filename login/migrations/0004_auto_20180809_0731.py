# Generated by Django 2.0.7 on 2018-08-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user_accesstoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='accesstoken',
            new_name='accesstoken_facebook',
        ),
        migrations.AddField(
            model_name='user',
            name='accesstoken_kakao',
            field=models.CharField(default='charField', max_length=200),
        ),
    ]
