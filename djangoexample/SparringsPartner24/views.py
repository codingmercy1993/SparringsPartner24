from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

# Create your views here.

from django.http import HttpResponse

from .forms import FighterProfileForm, UserProfileForm, SearchProfileForm, SearchEngineForm
from .models import UserProfile, FighterProfile, SearchProfile

def index(request):
    return render(request, 'SparringsPartner24/Index.html')

def fighter_profile(request, userprofile_id):
    result = FighterProfile.objects.select_related("userprofile").get(pk=userprofile_id)

    return render(request, 'SparringsPartner24/fighter_profile.html', {'profile': result})

def search_engine(request):
    if request.method == 'POST':
        form = SearchEngineForm(request.POST)
        if form.is_valid():
            
            result_list = FighterProfile.objects.filter(Q(Weight__gte = form.cleaned_data['MinWeight']) | Q(Weight__lte = form.cleaned_data['MaxWeight']),
                    MartialArt = form.cleaned_data['MartialArt'])
                # weitere kriterien fehlen
            result_list = FighterProfile.objects.all()

            return render(request, 'SparringsPartner24/search_engine_result.html', {'result_list': result_list})
    else:
        form = SearchEngineForm()
        
    return render(request, 'SparringsPartner24/create_profile.html', {'form': form})


def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            task = form.save(commit=True)
            
            return HttpResponseRedirect(reverse('SparringsPartner24:create_fighter_profile', args=(task.id,)))
            
    else:
        form = UserProfileForm()

    return render(request, 'SparringsPartner24/create_profile.html', {'form': form})

def edit_user_profile(request, userprofile_id):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            task = form.save(commit=True)
            
            return HttpResponseRedirect(reverse('SparringsPartner24:index'))
    else:
        user_profile = get_object_or_404(UserProfile, pk = userprofile_id)
        form = UserProfileForm(instance = user_profile)
        return render(request, 'SparringsPartner24/create_profile.html', {'form': form})



def create_fighter_profile(request, userprofile_id):
    if request.method == 'POST':
        form = FighterProfileForm(request.POST)
    
        if form.is_valid():

            updated_form = form.save(commit = False)
            userprofile_object = get_object_or_404(UserProfile, pk = userprofile_id)
            updated_form.userprofile = userprofile_object
            updated_form.save()

            return HttpResponseRedirect(reverse('SparringsPartner24:create_search_profile', args=(userprofile_object.id,)))
            
    else:
        form = FighterProfileForm()
    return render(request, 'SparringsPartner24/create_profile.html', {'form': form})

def edit_fighter_profile(request, userprofile_id):
    if request.method == 'POST':
        form = FighterProfileForm(request.POST)
    
        if form.is_valid():

            updated_form = form.save(commit = False)
            userprofile_object = get_object_or_404(UserProfile, pk = userprofile_id)
            updated_form.userprofile = userprofile_object
            updated_form.save()

            return HttpResponseRedirect(reverse('SparringsPartner24:index'))
            
    else:
        fighter_profile = get_object_or_404(FighterProfile, pk = userprofile_id)
        form = FighterProfileForm(instance = fighter_profile)
        return render(request, 'SparringsPartner24/create_profile.html', {'form': form})


def create_search_profile(request, userprofile_id):
    if request.method == 'POST':
        form = SearchProfileForm(request.POST)
    
        if form.is_valid():

            updated_form = form.save(commit = False)
            updated_form.userprofile = get_object_or_404(UserProfile, pk = userprofile_id)
            updated_form.save()

            return HttpResponseRedirect(reverse('SparringsPartner24:index'))
            
    else:
        form = SearchProfileForm()

    return render(request, 'SparringsPartner24/create_profile.html', {'form': form})

def edit_search_profile(request, userprofile_id):
    if request.method == 'POST':
        form = SearchProfileForm(request.POST)
    
        if form.is_valid():

            updated_form = form.save(commit = False)
            updated_form.userprofile = get_object_or_404(UserProfile, pk = userprofile_id)
            updated_form.save()

            return HttpResponseRedirect(reverse('SparringsPartner24:index'))
            
    else:
        search_profile = get_object_or_404(SearchProfile, pk = userprofile_id)
        form = SearchProfileForm(instance = search_profile)
        return render(request, 'SparringsPartner24/create_profile.html', {'form': form})

