# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-16 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_platform', '0026_auto_20190516_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='production',
            field=models.CharField(choices=[('indie', 'Indie'), ('professional', 'Professional')], default=None, max_length=100),
        ),
    ]