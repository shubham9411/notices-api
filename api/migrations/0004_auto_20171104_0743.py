# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-04 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171104_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='choices',
            field=models.CharField(choices=[('Official', 'Official'), ('Branch', 'Branch'), ('All', 'All')], default='All', max_length=3, null=True),
        ),
    ]
