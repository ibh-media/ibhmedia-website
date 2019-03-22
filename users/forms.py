from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserChangeForm

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
        fields = ('gender', 'birthdate', 'plan')

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
        # PLAN CHECK
        '''
        if profile.plan == "Pro":
            valid_cc = False
            if valid_cc:
                profile.save()

        elif created and profile.plan == "Free": # This prevents saving if profile already exist
            profile.save()
        '''
        if created:
            profile.save()

class EditUserForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'plan',
        )
