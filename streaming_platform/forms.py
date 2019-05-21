from django import forms
from .models import Song, Movie, Podcast

class DateInput(forms.DateInput):
    input_type = 'date'

class MusicForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'author', 'thumbnail', 'video_file', )

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'director', 'year_of_release', 'genres' ,'production', 'summary', 'thumbnail', 'video_file',  )

class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ('title', 'author', 'publication', 'thumbnail', 'audio_file', )