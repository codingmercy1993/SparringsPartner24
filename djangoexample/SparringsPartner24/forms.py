from django import forms

from .models import UserProfile, FighterProfile, SearchProfile

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
    MinAge = forms.IntegerField()
    MaxAge = forms.IntegerField()
    MinWeight = forms.IntegerField()
    MaxWeight = forms.IntegerField()

    choices_dict = [('boxen', 'Boxen'), ('thai', 'Thai'), ('mma', 'MMA')]
    MartialArt = forms.CharField(widget = forms.SelectMultiple(choices = choices_dict) )
    MaxDistance = forms.IntegerField()
    MinNumberFights = forms.IntegerField()
    MaxNumberFights = forms.IntegerField()