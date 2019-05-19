from .models import Movie
import django_filters

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

    genre1 = django_filters.ChoiceFilter(choices=MOVIE_GENERES)
    genre2 = django_filters.ChoiceFilter(choices=MOVIE_GENERES)
    genre3 = django_filters.ChoiceFilter(choices=MOVIE_GENERES)

    class Meta:
        model = Movie
        fields = ['title', 'director', 'year__gte', 'year__lte', 'genre1', 'genre2', 'genre3', 'production']