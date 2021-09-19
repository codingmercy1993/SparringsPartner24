from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile, FighterProfile, SearchProfile
from django.contrib.auth.forms import UserCreationForm
import os
from functools import lru_cache

martial_art_choices = [('Boxen', 'Boxen'), ('Thai', 'Thai'), ('MMA', 'MMA'), ('BJJ', 'BJJ'), ("Kickboxing", "Kickboxing"), ("Bareknuckle", "Bareknuckle")]
all_martial_art_choices = [('Alle', 'Alle'), ('Boxen', 'Boxen'), ('Thai', 'Thai'), ('MMA', 'MMA'), ('BJJ', 'BJJ'), ("Kickboxing", "Kickboxing"), ("Bareknuckle", "Bareknuckle")]

gender_choices = [('Male', 'Male'), ('Female', 'Female'), ('Diverse', 'Diverse')]
all_gender_choices = [('Alle', 'Alle'),('Male', 'Male'), ('Female', 'Female'), ('Diverse', 'Diverse')]

@lru_cache()
def _get_city_choices(add_string = False):
    with open(os.path.dirname(__file__) + "/city_list.txt") as file:
       lines = file.readlines()
       lines = [line.rstrip() for line in lines]
       city_choices = []
       if add_string:
           city_choices.append(('Alle', 'Alle'))
       for i in lines:
           city_choices.append((i, i))


    return city_choices

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

    martial_art = forms.ChoiceField(choices=all_martial_art_choices, required=False)
    location = forms.ChoiceField(choices=_get_city_choices(), required=False)
    gender = forms.ChoiceField(choices=gender_choices, required=False)


class SearchProfileForm(forms.ModelForm):
    class Meta:
        model = SearchProfile
        exclude = ['userprofile']
    gender = forms.ChoiceField(choices=all_gender_choices, required=False)
    martial_art = forms.ChoiceField(choices=all_martial_art_choices, required=False)

class SearchEngineForm(forms.Form):
    max_distance = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'type':'range', 'step': '2'}))
    martial_art = forms.ChoiceField(choices=all_martial_art_choices, required=False)
    location = forms.ChoiceField(choices=_get_city_choices(True), required=False)
    gender = forms.ChoiceField(choices=all_gender_choices, required=False)
    max_weight = forms.IntegerField(required=False, initial = 100)
    min_weight = forms.IntegerField(required=False, initial = 0)
    
    max_age = forms.IntegerField(required=False, initial = 70)
    min_age = forms.IntegerField(required=False, initial = 0)
    
    max_fights = forms.IntegerField(required=False, initial = 200 )
    min_fights = forms.IntegerField(required=False, initial = 0)

    max_experience_years = forms.IntegerField(required = False, initial = 50)
    min_experience_years = forms.IntegerField(required = False, initial = 0)



