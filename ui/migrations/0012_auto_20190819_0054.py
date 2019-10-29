# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-08-19 04:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0011_auto_20190818_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queue',
            name='env',
        ),
        migrations.AddField(
            model_name='protocol',
            name='env',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ui.VirtualEnvironment'),
        ),
    ]