from django.conf.urls import url, include;
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^edit/', views.edit_profile, name='edit_profile'),
]

urlpatterns += staticfiles_urlpatterns()