# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
import datetime

from multiselectfield import MultiSelectField

from django.contrib.auth.models import User
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
    # Categories/Filters
    MOVIE_GENERES =    (('-------', '-------'),
                        ('Comedy', 'Comedy'),
                        ('Kids', 'Kids'),
                        ('Action', 'Action'),
                        ('Teen', 'Teen'),
                        ('Drama', 'Drama'))

    MOVIE_PRODUCTION = (('Indie', 'Indie'),
                        ('Professional', 'Professional'))

    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100, default=None)
    duration = models.CharField(max_length=8)
    summary = models.TextField(max_length=300, default=None)
    year_of_release = models.IntegerField(choices=[(r,r) for r in range(1920, datetime.date.today().year+1)], default=datetime.date.today().year)
    genres = MultiSelectField(choices=MOVIE_GENERES, max_choices=5)
    production = models.CharField(max_length=100, choices=MOVIE_PRODUCTION, default=None)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='movie_thumbnails', default='not found', blank=False)
    video_file = models.FileField(upload_to='movies/', default='not found', blank=True)

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
    publication = models.CharField(max_length=100)
    duration = models.CharField(max_length=8)
    release_date = models.DateField(default=datetime.date.today)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='podcast_thumbnail', blank=False)
    audio_file = models.FileField(upload_to='podcast_audio/', default='not found', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Podcast, self).save(*args, **kwargs)

class Favorite(models.Model):
    current_user = models.ForeignKey(User, related_name='owner')
    tv_channels = models.ManyToManyField(TV_channel, related_name='tv_channel_set', blank=True)
    movies = models.ManyToManyField(Movie, related_name='movie_set', blank=True)
    songs = models.ManyToManyField(Song, related_name='song_set', blank=True)
    podcasts = models.ManyToManyField(Podcast, related_name='podcast_set', blank=True)

    @classmethod
    def make_favorite(cls, current_user, new_favorite):
        favorite, created = cls.objects.get_or_create(
            current_user = current_user
        )
        if isinstance(new_favorite, TV_channel):
            favorite.tv_channels.add(new_favorite)
        elif isinstance(new_favorite, Movie):
            favorite.movies.add(new_favorite)
        elif isinstance(new_favorite, Song):
            favorite.songs.add(new_favorite)
        elif isinstance(new_favorite, Podcast):
            favorite.podcasts.add(new_favorite)

    @classmethod
    def delete_favorite(cls, current_user, new_favorite):
        favorite, created = cls.objects.get_or_create(
            current_user = current_user
        )
        if isinstance(new_favorite, TV_channel):
            favorite.tv_channels.remove(new_favorite)
        elif isinstance(new_favorite, Movie):
            favorite.movies.remove(new_favorite)
        elif isinstance(new_favorite, Song):
            favorite.songs.remove(new_favorite)
        elif isinstance(new_favorite, Podcast):
            favorite.podcasts.remove(new_favorite)