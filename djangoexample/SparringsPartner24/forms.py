from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile, FighterProfile, SearchProfile
from django.contrib.auth.forms import UserCreationForm


martial_art_choices = [('boxen', 'Boxen'), ('thai', 'Thai'), ('mma', 'MMA'), ('bjj', 'BJJ'), ("kickboxing", "Kickboxing"), ("bareknuckle", "Bareknuckle")]

#with open("/city_list.txt") as file:
#    lines = file.readlines()
#    lines = [line.rstrip() for line in lines]

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
        fields = ('username', 'email', 'phone_number', 'first_name', 'last_name')

class FighterProfileForm(forms.ModelForm):
    class Meta:
        model = FighterProfile
        exclude = ['userprofile']

    martial_art = forms.ChoiceField(choices=martial_art_choices, required=False)


class SearchProfileForm(forms.ModelForm):
    class Meta:
        model = SearchProfile
        exclude = ['userprofile']

class SearchEngineForm(forms.Form):
    max_distance = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'type':'range', 'step': '2'}))
    martial_art = forms.ChoiceField(choices=martial_art_choices, required=False)

    max_weight = forms.IntegerField(required=False, initial = 100)
    min_weight = forms.IntegerField(required=False, initial = 0)
    
    max_age = forms.IntegerField(required=False, initial = 70)
    min_age = forms.IntegerField(required=False, initial = 0)
    
    max_fights = forms.IntegerField(required=False, initial = 200 )
    min_fights = forms.IntegerField(required=False, initial = 0)

    max_experience_years = forms.IntegerField(required = False, initial = 50)
    min_experience_years = forms.IntegerField(required = False, initial = 0)



