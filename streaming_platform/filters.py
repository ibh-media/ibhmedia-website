from .models import Movie
import django_filters
from django import forms
from operator import and_, or_
from django.db.models import Q

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    director = django_filters.CharFilter(lookup_expr='icontains')

    year__gte = django_filters.NumberFilter(field_name='year_of_release', lookup_expr='gte')
    year__lte = django_filters.NumberFilter(field_name='year_of_release', lookup_expr='lte')
    
    MOVIE_GENERES = (('Comedy', 'Comedy'),
                     ('Kids', 'Kids'),
                     ('Action', 'Action'),
                     ('Teen', 'Teen'),
                     ('Drama', 'Drama'))

    genres = django_filters.MultipleChoiceFilter(choices=MOVIE_GENERES, method='filter_genres', widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Movie
        fields = ['title', 'director', 'year__gte', 'year__lte', 'genres', 'production']

    def filter_genres(self, queryset, name, genres):
        return queryset.filter(reduce(or_, [Q(genres__icontains=q) for q in genres]))
