# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_delivery_zipcode',
            field=models.IntegerField(blank=True),
        ),
    ]