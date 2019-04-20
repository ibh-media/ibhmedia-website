# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Import models and forms
from .models import TV_channel, Movie, Song, Podcast
from .forms import MusicForm, MovieForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url="/accounts/login")
def tv(request):
    tv_channels = TV_channel.objects.all().order_by('live') # order by any variable in Movie class from models 
    return render(request, 'tv.html', {'tv_channels': tv_channels})

@login_required(login_url="/accounts/login")
def movies(request):
    movies = Movie.objects.all().order_by('release_date') 
    return render(request, 'movies.html', {'movies': movies})

@staff_member_required(login_url="/movies")
def movie_upload(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/movies')
    else:
        form = MovieForm()
    return render(request, 'movie_upload.html', {'form': form})

@login_required(login_url="/accounts/login")
def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    return render(request, 'movie_detail.html', {'movie': movie})

@login_required(login_url="/accounts/login")
def songs(request):
    songs = Song.objects.all().order_by('release_date')
    return render(request, 'music.html', {'songs': songs})

@login_required(login_url="/accounts/login")
def music_upload(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/music')
    else:
        form = MusicForm()
    return render(request, 'music_upload.html', {'form': form})

@login_required(login_url="/accounts/login")
def music_detail(request, slug):
    song = Song.objects.get(slug=slug)
    return render(request, 'music_detail.html', {'song': song})

@login_required(login_url="/accounts/login")
def podcasts(request):
    podcasts = Podcast.objects.all().order_by('release_date') 
    return render(request, 'podcasts.html', {'podcasts': podcasts})

