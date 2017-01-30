# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-30 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170129_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brewpidevice',
            name='script_path',
        ),
        migrations.AddField(
            model_name='brewpidevice',
            name='do_not_run',
            field=models.BooleanField(default=False),
        ),
    ]