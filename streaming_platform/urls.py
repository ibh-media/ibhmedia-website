from django.conf.urls import url, include;
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^tv/$', views.tv, name='tv'),
    url(r'^movies/$', views.movies, name='movies'),
    url(r'^movies/movie_upload/$', views.movie_upload, name='movie_upload'),
    url(r'^movies/filter/$', views.movies, name='movies'),
    url(r'^movies/(?P<slug>[\w-]+)/$', views.movie_detail, name='movie_detail'),
    url(r'^music/$', views.songs, name='songs'),
    url(r'^music/music_upload/$', views.music_upload, name='music_upload'),
    url(r'^music/(?P<slug>[\w-]+)/$', views.music_detail, name='music_detail'),
    url(r'^podcasts/$', views.podcasts, name='podcasts'),
    url(r'^podcasts/podcast_upload/$', views.podcast_upload, name='podcast_upload'),
    url(r'^podcasts/(?P<slug>[\w-]+)/$', views.podcast_detail, name='podcast_detail'),

    url(r'^mypixs/$', views.favorites, name='favorites'),
    url(r'^mypixs/(?P<operation>.+)/(?P<content_type>.+)/(?P<slug>[\w-]+)', views.change_favorite, name='change_favorite')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)