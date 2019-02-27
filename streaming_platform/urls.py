from django.conf.urls import url, include;
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tv/', views.tv, name='tv'),
    url(r'^movies/', views.movies, name='movies'),
    url(r'^videos/', views.videos, name='videos'),
    url(r'^podcasts/', views.podcasts, name='podcasts'),
]

urlpatterns += staticfiles_urlpatterns()