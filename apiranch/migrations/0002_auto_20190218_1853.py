# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-18 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiranch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plugin',
            name='plugin_version',
        ),
        migrations.AddField(
            model_name='plugin',
            name='plugin_version',
            field=models.ManyToManyField(to='apiranch.plugin_version'),
        ),
        migrations.RemoveField(
            model_name='render_engien',
            name='render_engien_version',
        ),
        migrations.AddField(
            model_name='render_engien',
            name='render_engien_version',
            field=models.ManyToManyField(to='apiranch.render_engien_version'),
        ),
        migrations.RemoveField(
            model_name='software',
            name='software_version',
        ),
        migrations.AddField(
            model_name='software',
            name='software_version',
            field=models.ManyToManyField(to='apiranch.softwareVersion'),
        ),
        migrations.RemoveField(
            model_name='softwareversion',
            name='render_engien',
        ),
        migrations.AddField(
            model_name='softwareversion',
            name='render_engien',
            field=models.ManyToManyField(to='apiranch.render_engien'),
        ),
    ]
