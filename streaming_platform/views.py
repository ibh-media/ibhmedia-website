# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Import models
from .models import TV_channel, Movie, Song, Podcast, Favorite

# Import forms
from .forms import MusicForm, MovieForm, PodcastForm

# Import filters
from .filters import MovieFilter

from django.apps import apps

# Views.
def index(request):
    return render(request, 'index.html')

# CONTENT
# TV
@login_required(login_url="/accounts/login")
def tv(request):
    tv_channels = TV_channel.objects.all().order_by('live') # order by any variable in Movie class from models 
    return render(request, 'tv/tv.html', {'tv_channels': tv_channels})

# Movies
@login_required(login_url="/accounts/login")
def movies(request):
    movies = Movie.objects.all().order_by('-year_of_release')
    movie_filter = MovieFilter(request.GET, queryset=movies)

    return render(request, 'movies/movies.html', {'movies': movies, 'filter': movie_filter})

@staff_member_required(login_url="/movies")
def movie_upload(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/movies')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_upload.html', {'form': form})

@login_required(login_url="/accounts/login")
def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    favorite = Favorite.objects.get(current_user=request.user)
    favorite_movies = favorite.movies.all()
    args = {
        'movie': movie,
        'favorite_movies': favorite_movies
    }
    return render(request, 'movies/movie_detail.html', args)

# Music
@login_required(login_url="/accounts/login")
def songs(request):
    songs = Song.objects.all().order_by('release_date')
    return render(request, 'music/music.html', {'songs': songs})

@login_required(login_url="/accounts/login")
def music_upload(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/music')
    else:
        form = MusicForm()
    return render(request, 'music/music_upload.html', {'form': form})

@login_required(login_url="/accounts/login")
def music_detail(request, slug):
    song = Song.objects.get(slug=slug)
    favorite = Favorite.objects.get(current_user=request.user)
    favorite_songs = favorite.songs.all()
    args = {
        'song': song,
        'favorite_songs': favorite_songs
    }
    return render(request, 'music/music_detail.html', args)

# Podcasts
@login_required(login_url="/accounts/login")
def podcasts(request):
    podcasts = Podcast.objects.all().order_by('release_date') 
    return render(request, 'podcasts/podcasts.html', {'podcasts': podcasts})

@login_required(login_url="/accounts/login")
def podcast_upload(request):
    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/podcasts')
    else:
        form = PodcastForm()
    return render(request, 'podcasts/podcast_upload.html', {'form': form})

@login_required(login_url="/accounts/login")
def podcast_detail(request, slug):
    podcast = Podcast.objects.get(slug=slug)
    favorite = Favorite.objects.get(current_user=request.user)
    favorite_podcasts = favorite.podcasts.all()
    args = {
        'podcast': podcast,
        'favorite_podcasts': favorite_podcasts
    }
    return render(request, 'podcasts/podcast_detail.html', args)

# Favorites
@login_required(login_url='/accounts/login')
def favorites(request):
    favorite, created = Favorite.objects.get_or_create(current_user=request.user)
    
    favorite_tv_channels = favorite.tv_channels.all()
    favorite_movies = favorite.movies.all()
    favorite_songs = favorite.songs.all()
    favorite_podcasts = favorite.podcasts.all()

    args = {
        'favorite_tv_channels': favorite_tv_channels, 
        'favorite_movies': favorite_movies, 
        'favorite_songs': favorite_songs,
        'favorite_podcasts': favorite_podcasts
    }
    
    return render(request, 'favorites.html', args)

@login_required(login_url="/accounts/login")
def change_favorite(request, operation, content_type, slug):
    model = apps.get_model('streaming_platform', content_type)
    new_favorite = model.objects.get(slug=slug)
    if operation == 'add':
        Favorite.make_favorite(request.user, new_favorite)
        
    elif operation == 'remove':
        Favorite.delete_favorite(request.user, new_favorite)
        
    return render(request, 'index.html')