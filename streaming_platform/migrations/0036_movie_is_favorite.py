# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_platform', '0035_auto_20190529_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
