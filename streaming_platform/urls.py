from django.conf.urls import url, include;
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about')
]

urlpatterns += staticfiles_urlpatterns()