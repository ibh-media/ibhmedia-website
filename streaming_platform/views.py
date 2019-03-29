# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Import models
from .models import TV_channel
from .models import Movie
from .models import Song
from .models import Podcast

from .forms import MusicForm

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

