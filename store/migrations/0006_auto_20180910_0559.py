# Generated by Django 2.0.7 on 2018-09-10 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_storereview_storepoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storereview',
            name='storepoint',
            field=models.IntegerField(default='5', max_length=200),
        ),
    ]