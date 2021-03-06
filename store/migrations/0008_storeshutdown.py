# Generated by Django 2.0.7 on 2018-09-10 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_remove_user_userid'),
        ('store', '0007_auto_20180910_0601'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreShutdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=200)),
                ('storeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
    ]
