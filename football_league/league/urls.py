from django.urls import path
from . import views

app_name = 'league'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:liga_id>/', views.leagues, name='leagues'),
    path('liga/<int:klub_id>/', views.clubs, name='clubs'),
    path('liga/pilkarz/<int:pilkarz_id>/', views.players, name='players'),
    path('liga/stadion/<int:stadion_id>/', views.stadions, name='stadions'),
    path('liga/trener/<int:trener_id>/', views.coach, name='coach'),
    path('liga/mecz/<int:mecz_id>/', views.mecz, name='mecz'),
    path('liga/mecze/', views.mecze, name='mecze'),
    path('liga/pilkarz/dodaj/', views.dodajPilkarza, name='dodajPilkarza'),
    path('liga/klub/dodaj/', views.dodajKlub, name='dodajKlub'),
    path('liga/pilkarz/<int:pilkarz_id>/edytuj/', views.edytujPilkarza, name='edytujPilkarza'),
    path('liga/<int:klub_id>/edytuj/', views.edytujKlub, name='edytujKlub'),
    path('liga/pilkarz/<int:pilkarz_id>/usun/', views.usunPilkarza, name='usunPilkarza'),
    path('liga/<int:klub_id>/usun/', views.usunKlub, name='usunKlub'),
]