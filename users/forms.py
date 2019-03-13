from django import forms
from .models import Profile

class DateInput(forms.DateInput):
    input_type = 'date'

class SignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        widgets = {
            'birthdate': DateInput()
        }
        fields = ('gender', 'birthdate','plan')

    # A custom method required to work with django-allauth, see https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
    def signup(self, request, user):
        # Save your user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile, created = Profile.objects.get_or_create(
            user=user, defaults={
                'gender': self.cleaned_data['gender'],
                'birthdate': self.cleaned_data['birthdate'],
                'plan': self.cleaned_data['plan'],
            })
        if created: # This prevents saving if profile already exist
            profile.save()
        '''
        # Save your profile
        profile = Profile()
        profile.user = user
        profile.gender = self.cleaned_data['gender']
        profile.birthdate = self.cleaned_data['birthdate']
        profile.plan = self.cleaned_data['plan']
        profile.save()
        '''