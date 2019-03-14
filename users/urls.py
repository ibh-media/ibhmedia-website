from django.conf.urls import url, include;
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^update', views.update_profile, name='update_profile'),
]

urlpatterns += staticfiles_urlpatterns()