# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from forms import EditProfileForm

def profile(request):
    return render(request, 'profile.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')