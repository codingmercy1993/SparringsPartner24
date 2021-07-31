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
        exclude = ['userprofile']

class SearchProfileForm(forms.ModelForm):
    class Meta:
        model = SearchProfile
        exclude = ['userprofile']

class SearchEngineForm(forms.Form):
    MinAge = forms.IntegerField(required=False)
    MaxAge = forms.IntegerField(required=False)
    MinWeight = forms.IntegerField(required=False)
    MaxWeight = forms.IntegerField(required=False)

    choices_dict = [('boxen', 'Boxen'), ('thai', 'Thai'), ('mma', 'MMA')]
    MartialArt = forms.CharField(widget = forms.SelectMultiple(choices = choices_dict), required=False )
    MaxDistance = forms.IntegerField(required=False)
    MinNumberFights = forms.IntegerField(required=False)
    MaxNumberFights = forms.IntegerField(required=False)
