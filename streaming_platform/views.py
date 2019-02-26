# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'streaming_platform/index.html')

def about(request):
    return render(request, 'streaming_platform/about.html')