# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .forms import EditUserForm, EditProfileForm

def profile(request):
    return render(request, 'profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('/accounts/profile')
    else:
        form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)
        args = {'form': form, 'profile_form': profile_form}
        return render(request, 'edit_profile.html', args)