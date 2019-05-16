from django import forms
from .models import Song, Movie

class DateInput(forms.DateInput):
    input_type = 'date'

class MusicForm(forms.ModelForm):
    class Meta:
        model = Song
        widgets = {
            'release_date': DateInput(),
        }
        fields = ('title', 'author', 'thumbnail', 'video_file', )

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'director', 'year_of_release', 'genres', 'production', 'summary', 'thumbnail', 'video_file',  )