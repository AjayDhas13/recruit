# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-20 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlpanel', '0002_auto_20180720_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]