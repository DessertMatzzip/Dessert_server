# Generated by Django 2.0.7 on 2018-08-30 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_storereview'),
        ('login', '0007_user_userid'),
        ('user', '0002_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='WantToGo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
                ('wantstoreid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
            ],
        ),
    ]