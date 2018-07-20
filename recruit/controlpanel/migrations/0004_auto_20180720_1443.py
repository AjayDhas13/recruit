# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-20 09:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlpanel', '0003_auto_20180720_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='ref_id',
            field=models.CharField(default=datetime.datetime(2018, 7, 20, 14, 43, 49, 353000), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.IntegerField(choices=[(0, 'submitted'), (1, 'viewed'), (2, 'accepted'), (3, 'rejected')], default=0),
        ),
    ]