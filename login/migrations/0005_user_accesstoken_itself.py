# Generated by Django 2.0.7 on 2018-08-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20180809_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accesstoken_itself',
            field=models.CharField(default='charField', max_length=200),
        ),
    ]
