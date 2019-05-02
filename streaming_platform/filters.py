from .models import Movie
import django_filters

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = {
            'title': ['contains'],
            'director': ['contains'],
            'release_date': ['year__lt', 'year__gt'],
        }