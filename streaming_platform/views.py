# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Import models
from .models import TV_channel
from .models import Movie
from .models import Video
from .models import Podcast

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
def videos(request):
    videos = Video.objects.all().order_by('release_date')
    return render(request, 'videos.html', {'videos': videos})

@login_required(login_url="/accounts/login")
def podcasts(request):
    podcasts = Podcast.objects.all().order_by('release_date') 
    return render(request, 'podcasts.html', {'podcasts': podcasts})