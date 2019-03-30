from django import forms
from .models import Song

class DateInput(forms.DateInput):
    input_type = 'date'

class MusicForm(forms.ModelForm):
    class Meta:
        model = Song
        widgets = {
            'release_date': DateInput(),
        }
        fields = ('title', 'author', 'thumbnail', 'video_file', )