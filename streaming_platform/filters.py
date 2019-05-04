from .models import Movie
import django_filters
'''
class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = {
            'title': ['contains'],
            'director': ['contains'],
            'release_date': ['year__lt', 'year__gt'],
        }
'''

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    director = django_filters.CharFilter(lookup_expr='icontains')

    #year__gt = django_filters.NumberFilter(field_name='year_of_release', lookup_expr='gt')
    #year__lt = django_filters.NumberFilter(field_name='year_of_release', lookup_expr='lt')
    
    class Meta:
        model = Movie
        fields = ['title', 'director'] # add this to fields for yea rof release filter -- 'year__gt', 'year__lt'