# Generated by Django 2.0.7 on 2018-08-30 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0007_user_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collectionname', models.CharField(max_length=200)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
    ]
