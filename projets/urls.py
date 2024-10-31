# projets/urls.py
from django.urls import path
from .views import liste_projets, creer_projet, creer_tache

urlpatterns = [
    path('', liste_projets, name='liste_projets'),
    path('creer/', creer_projet, name='creer_projet'),
    path('creer_tache/<int:projet_id>/', creer_tache, name='creer_tache'),
]
