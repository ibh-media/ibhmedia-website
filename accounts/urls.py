from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login, name='login'),
]

urlpatterns += staticfiles_urlpatterns()