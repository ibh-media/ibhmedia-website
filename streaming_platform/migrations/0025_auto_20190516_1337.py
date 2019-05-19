# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-16 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streaming_platform', '0024_auto_20190505_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre1',
            field=models.CharField(choices=[('comedy', 'Comedy'), ('kids', 'Kids'), ('action', 'Action'), ('teen', 'Teen'), ('drama', 'Drama')], default=None, max_length=100, verbose_name='Main genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre2',
            field=models.CharField(choices=[('comedy', 'Comedy'), ('kids', 'Kids'), ('action', 'Action'), ('teen', 'Teen'), ('drama', 'Drama')], default=None, max_length=100, verbose_name='Sub-genre 1'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre3',
            field=models.CharField(choices=[('comedy', 'Comedy'), ('kids', 'Kids'), ('action', 'Action'), ('teen', 'Teen'), ('drama', 'Drama')], default=None, max_length=100, verbose_name='Sub-genre 2'),
        ),
        migrations.AddField(
            model_name='movie',
            name='production',
            field=models.CharField(choices=[('indie', 'Indie'), ('professional', 'Professional')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='summary',
            field=models.TextField(default=None, max_length=300),
        ),
    ]
