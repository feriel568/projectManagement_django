from django.urls import path
from . import views

app_name = 'utilisateurs'

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.UtilisateurConnexionView.as_view(), name='connexion'),
    path('deconnexion/', views.UtilisateurDeconnexionView.as_view(), name='logout'),
    path('', views.home, name='home'),
]
