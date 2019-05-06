from .models import Movie
import django_filters

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    director = django_filters.CharFilter(lookup_expr='icontains')

    year__gte = django_filters.NumberFilter(field_name='year_of_release', lookup_expr='gte')
    year__lte = django_filters.NumberFilter(field_name='year_of_release', lookup_expr='lte')
    
    class Meta:
        model = Movie
        fields = ['title', 'director', 'year__gte', 'year__lte'] # add this to fields for yea rof release filter -- 'year__gt', 'year__lt' 