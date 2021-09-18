import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth import login
from datetime import date
# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import FighterProfileForm, UserProfileForm, SearchProfileForm, SearchEngineForm, UserProfileCreationForm
from .models import UserProfile, FighterProfile, SearchProfile

def index(request):

    if request.user.is_authenticated:
        # flag iwann wo profile createn kann
        current_user = request.user
        has_fighterprofile = UserProfile.objects.filter(fighterprofile__isnull=False, id = current_user.id).exists()
        has_searchprofile = UserProfile.objects.filter(searchprofile__isnull=False, id = current_user.id).exists()
        
        return render(request, "SparringsPartner24/Index.html", {"has_fighterprofile": has_fighterprofile, "has_searchprofile": has_searchprofile})

    return render(request, 'SparringsPartner24/Index.html')

def register(request):
    if request.method == "GET":
        return render(
            request, "SparringsPartner24/register.html",
            {"form": UserProfileCreationForm}
        )
    elif request.method == "POST":
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return render(request, 'SparringsPartner24/Index.html')

@login_required
def fighter_profile(request, userprofile_id):
    result = FighterProfile.objects.select_related("userprofile").get(pk=userprofile_id)
    result.age = _birthday_to_age(result.birthday)
    search_profile = SearchProfile.objects.get(pk=userprofile_id)

    return render(request, 'SparringsPartner24/fighter_profile_new.html', {'profile': result, 'searchprofile': search_profile})

@login_required
def search_engine(request):
    if request.method == 'POST':
        form = SearchEngineForm(request.POST)
        if form.is_valid():
            
            filters = {}
            for key, value in request.POST.items():
                print(key, value)
                if value:

                    if key == 'max_weight':
                        filters['weight__lte'] = value
                    elif key == 'min_weight':
                        filters['weight__gte'] = value

                    elif key == 'max_age':
                        filters['birthday__gte'] = _age_to_birthday(value)
                    elif key == 'min_age':
                        filters['birthday__lte'] = _age_to_birthday(value)

                    elif key == 'max_fights':
                        filters['fight_record__lte'] = value
                    elif key == 'min_fights':
                        filters['fight_record__gte'] = value
                    
                    elif key == 'max_experience_years':
                        filters['experience_years__lte'] = value
                    elif key == 'min_experience_years':
                        filters['experience_years__gte'] = value

                    elif key == 'location':
                        if value != 'Alle':
                            filters['location__icontains'] = value
                    
                    elif key == 'gender':
                        if value != 'Alle':
                            filters['gender__icontains'] = value
                    
                    elif key == 'martial_art':
                        filters['martial_art__icontains'] = value

            print(filters)
            result_list = FighterProfile.objects.filter(**filters)
            print(result_list)
            return render(request, 'SparringsPartner24/fighter_list.html', {'result_list': result_list})
    else:
        form = SearchEngineForm()
        
    return render(request, 'SparringsPartner24/search_engine.html', {'form': form})

@login_required
def edit_user_profile(request):
    current_user = request.user
    if request.method == 'POST':
        instance = get_object_or_404(UserProfile, pk = current_user.id)
        form = UserProfileForm(request.POST, instance = instance)
        if form.is_valid():

            form.save()
            
            return HttpResponseRedirect(reverse('SparringsPartner24:index'))
    else:
        user_profile = get_object_or_404(UserProfile, pk = current_user.id)
        form = UserProfileForm(instance = user_profile)
        return render(request, 'SparringsPartner24/create_profile.html', {'form': form})

@login_required
def edit_fighter_profile(request):
    current_user = request.user

    if request.method == 'POST':
        instance = get_object_or_404(FighterProfile, pk = current_user.id)
        form = FighterProfileForm(request.POST, instance = instance)
    
        if form.is_valid():

            updated_form = form.save(commit = False)
            userprofile_object = get_object_or_404(UserProfile, pk = current_user.id)
            updated_form.userprofile = userprofile_object
            updated_form.save()

            return HttpResponseRedirect(reverse('SparringsPartner24:index'))
            
    else:
        fighter_profile = get_object_or_404(FighterProfile, pk = current_user.id)
        form = FighterProfileForm(instance = fighter_profile)
        return render(request, 'SparringsPartner24/create_profile.html', {'form': form})

@login_required
def edit_search_profile(request):
    current_user = request.user
    if request.method == 'POST':
        instance = get_object_or_404(SearchProfile, pk = current_user.id)
        form = SearchProfileForm(request.POST, instance = instance )

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('SparringsPartner24:index'))
            
    else:
        search_profile = get_object_or_404(SearchProfile, pk = current_user.id)
        form = SearchProfileForm(instance = search_profile)
        return render(request, 'SparringsPartner24/create_profile.html', {'form': form})

@login_required
def get_all_fighters(request):
    result_list = FighterProfile.objects.select_related("userprofile").all()


    return render(request, 'SparringsPartner24/fighter_list.html', {'result_list': result_list})


def _birthday_to_age(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def _age_to_birthday(age):
    today = date.today()
    birthyear = today.year - int(age)
    birthday = datetime.datetime(year = birthyear, month=today.month, day=today.day)
    print(f"iih {birthday}")
    return birthday