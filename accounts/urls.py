from django.conf.urls import url, include;
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
]

urlpatterns += staticfiles_urlpatterns()