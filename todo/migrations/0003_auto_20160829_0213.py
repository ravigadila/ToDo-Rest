# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_list_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
