# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-18 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiranch', '0006_auto_20190218_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='render_engien',
            name='render_engien_version',
            field=models.ManyToManyField(blank=True, to='apiranch.render_engien_version'),
        ),
        migrations.AlterField(
            model_name='softwareversion',
            name='render_engien',
            field=models.ManyToManyField(blank=True, to='apiranch.render_engien'),
        ),
    ]
