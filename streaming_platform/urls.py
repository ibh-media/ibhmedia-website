from django.conf.urls import url, include;
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tv/$', views.tv, name='tv'),
    url(r'^movies/$', views.movies, name='movies'),
    url(r'^music/$', views.songs, name='songs'),
    url(r'^music/music_upload/$', views.music_upload, name='music_upload'),
    url(r'^music/(?P<slug>[\w-]+)/$', views.music_detail, name='music_detail'),
    url(r'^podcasts/$', views.podcasts, name='podcasts'),
]

urlpatterns += staticfiles_urlpatterns()