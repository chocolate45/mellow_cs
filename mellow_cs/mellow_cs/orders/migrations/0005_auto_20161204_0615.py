# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 05:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20161204_0613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'get_latest_by': 'order_date', 'ordering': ['-order_date']},
        ),
    ]