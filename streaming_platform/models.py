# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Movie(models.model):
    title = models.CharField()
    duration = models.TimeField()
    year = models.DateField()
    video_url = models.URLField()
    #add thumbnail