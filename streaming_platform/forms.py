from django import forms
from .models import Song

class MusicForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title', 'author', 'duration', 'release_date', 'thumbnail', )