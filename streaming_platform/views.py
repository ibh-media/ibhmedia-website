# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Import models
from .models import Movie
from .models import TV_channel

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tv(request):
    tv_channels = TV_channel.objects.all().order_by('live') # order by any variable in Movie class from models 
    return render(request, 'tv.html', {'tv_channels': tv_channels})

def movies(request):
    movies = Movie.objects.all().order_by('year') # order by any variable in Movie class from models 
    return render(request, 'movies.html', {'movies': movies})

def videos(request):
    return render(request, 'videos.html')

def podcasts(request):
    return render(request, 'podcasts.html')