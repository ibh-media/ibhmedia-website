# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
import datetime

'''
===== IMPORTANT =====
Every time you change/create a model:
    - python manage.py makemigrations
    - python manage.py migrate
'''

class TV_channel(models.Model):
    name = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    live = models.BooleanField()
    url = models.URLField(max_length=200, default='not_found')
    
    # shows name of channel in admin view
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100, default='not found')
    duration = models.CharField(max_length=8)
    release_date = models.DateField(default=datetime.date.today)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='movie_thumbnails', default='not found', blank=False)
    video_file= models.FileField(upload_to='movies/', default='not found', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

class Song(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    duration = models.CharField(max_length=8)
    release_date = models.DateField(default=datetime.date.today)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='music_thumbnails', blank=False)
    video_file= models.FileField(upload_to='videos/', default='not found', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Song, self).save(*args, **kwargs)

class Podcast(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=8)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    url = models.URLField(max_length=200)
    slug = models.SlugField(default='not_found')
    # add thumbnail

    def __str__(self):
        return self.title