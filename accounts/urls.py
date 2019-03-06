from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^login/', views.login_view, name='login'),
]

urlpatterns += staticfiles_urlpatterns()