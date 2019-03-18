# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import TV_channel
from .models import Movie
from .models import Song
from .models import Podcast

admin.site.register(TV_channel)
admin.site.register(Movie)
admin.site.register(Song)
admin.site.register(Podcast)