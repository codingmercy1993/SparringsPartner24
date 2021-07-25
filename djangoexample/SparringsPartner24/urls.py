from django.urls import path

from . import views

app_name = 'SparringsPartner24'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_user_profile/', views.create_user_profile, name = 'create_user_profile'),
    path('create_fighter_profile/<int:userprofile_id>/', views.create_fighter_profile, name = 'create_fighter_profile'),
    path('fighter_profile/<int:fighterprofile_id>/', views.fighter_profile, name='fighter_profile'),
    path('search_engine/', views.search_engine)

]
