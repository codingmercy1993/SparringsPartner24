from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile, FighterProfile, SearchProfile
from django.contrib.auth.forms import UserCreationForm


class UserProfileCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'email')

class UserProfileChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ('username', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class FighterProfileForm(forms.ModelForm):
    class Meta:
        model = FighterProfile
        exclude = ['userprofile', 'experience_years']

class SearchProfileForm(forms.ModelForm):
    class Meta:
        model = SearchProfile
        exclude = ['userprofile']

class SearchEngineForm(forms.Form):
    max_distance = forms.IntegerField(required=False)
    choices_dict = [('boxen', 'Boxen'), ('thai', 'Thai'), ('mma', 'MMA')]
    martial_art = forms.CharField(widget = forms.SelectMultiple(choices = choices_dict), required=False )

    max_weight = forms.IntegerField(required=False)
    min_weight = forms.IntegerField(required=False)
    
    max_age = forms.IntegerField(required=False)
    min_age = forms.IntegerField(required=False)
    
    max_fights = forms.IntegerField(required=False)
    min_fights = forms.IntegerField(required=False)

    max_experience_years = forms.IntegerField(required = False)
    min_experience_years = forms.IntegerField(required = False)



