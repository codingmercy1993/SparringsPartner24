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
    MinAge = forms.IntegerField(required=False)
    MaxAge = forms.IntegerField(required=False)
    MinWeight = forms.IntegerField(required=False)
    MaxWeight = forms.IntegerField(required=False)

    choices_dict = [('boxen', 'Boxen'), ('thai', 'Thai'), ('mma', 'MMA')]
    MartialArt = forms.CharField(widget = forms.SelectMultiple(choices = choices_dict), required=False )
    MaxDistance = forms.IntegerField(required=False)
    MinNumberFights = forms.IntegerField(required=False)
    MaxNumberFights = forms.IntegerField(required=False)
