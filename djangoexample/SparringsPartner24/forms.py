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
