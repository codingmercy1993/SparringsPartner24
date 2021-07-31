from django.urls import path, reverse_lazy
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'SparringsPartner24'
urlpatterns = [
    #path("accounts/", include(("django.contrib.auth.urls","accounts"), namespace="accounts")), muss auf obere ebene
    
    path('index', views.index, name='index'),
    path("register/", views.register, name = 'register'),
    path('create_user_profile/', views.create_user_profile, name = 'create_user_profile'),
    path('edit_user_profile/<int:userprofile_id>/', views.edit_user_profile, name = 'edit_user_profile'),
    path('create_fighter_profile/<int:userprofile_id>/', views.create_fighter_profile, name = 'create_fighter_profile'),
    path('edit_fighter_profile/<int:userprofile_id>/', views.edit_fighter_profile, name = 'edit_fighter_profile'),
    path('create_search_profile/<int:userprofile_id>/', views.create_search_profile, name = 'create_search_profile'),
    path('edit_search_profile/<int:userprofile_id>/', views.edit_search_profile, name = 'edit_search_profile'),
    path('fighter_profile/<int:userprofile_id>/', views.fighter_profile, name='fighter_profile'),
    path('search_engine/', views.search_engine, name = "search_engine"),
    path('get_all_fighters/', views.get_all_fighters, name = 'get_all_fighters')

]
