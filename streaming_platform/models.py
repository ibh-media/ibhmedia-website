# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

'''
===== IMPORTANT =====
Every time you change/create a model:
    - python manage.py makemigrations
    - python manage.py migrate
'''

class Movie(models.Model):
    title = models.CharField(max_length=200)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    year = models.DateField(auto_now=False, auto_now_add=False)
    url = models.URLField(max_length=200)
    #add thumbnail

    def __str__(self):
        return self.title