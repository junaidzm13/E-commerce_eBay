# Generated by Django 3.0.8 on 2020-07-11 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200712_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='active',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='winner',
        ),
    ]
