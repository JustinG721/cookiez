# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-03 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookiez', '0005_auto_20170503_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookie',
            name='imagePath',
            field=models.ImageField(default='/media/notAvailable.jpg', upload_to=b''),
        ),
    ]
