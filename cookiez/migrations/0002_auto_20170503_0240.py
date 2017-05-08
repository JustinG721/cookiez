# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-03 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookiez', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='streetone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='streettwo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='zipcode',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='cookie',
            name='cookieid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='custid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
