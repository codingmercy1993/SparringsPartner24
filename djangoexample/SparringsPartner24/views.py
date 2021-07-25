from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from django.http import HttpResponse

from .forms import FighterProfileForm, UserProfileForm, SearchProfileForm
from .models import UserProfile

def index(request):
    return HttpResponse("Was geht ^^ bist grad auf art website drauf")

def fighter_profile(request, fighterprofile_id):
    return HttpResponse("Fighterprofile")

def search_engine(request):
    return HttpResponse("search engine")


def create_user_profile(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # form.cleaned_data dann
            # process the data in form.cleaned_data as required
            task = form.save(commit=True)
            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('SparringsPartner24:create_fighter_profile', args=(task.id,)))
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserProfileForm()

    return render(request, 'SparringsPartner24/create_profile.html', {'form': form})

def create_fighter_profile(request, userprofile_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FighterProfileForm(request.POST)
    
        # check whether it's valid:
        if form.is_valid():

            updated_form = form.save(commit = False)
            updated_form.userprofile = UserProfile.objects.get(pk = userprofile_id)

            # form.cleaned_data dann
            # process the data in form.cleaned_data as required
            updated_form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('SparringsPartner24:index'))
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FighterProfileForm()

    return render(request, 'SparringsPartner24/create_profile.html', {'form': form})