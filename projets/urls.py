from django.urls import path
from .views import (
    liste_projets,
    creer_projet,
    creer_tache,
    editer_projet,
    supprimer_projet,
    editer_tache,
    supprimer_tache
)

urlpatterns = [
    path('', liste_projets, name='liste_projets'),
    path('creer/', creer_projet, name='creer_projet'),
    path('creer_tache/<int:projet_id>/', creer_tache, name='creer_tache'),
    # Edit and delete for projects
    path('editer_projet/<int:projet_id>/', editer_projet, name='editer_projet'),
    path('supprimer_projet/<int:projet_id>/', supprimer_projet, name='supprimer_projet'),
    # Edit and delete for tasks
    path('editer_tache/<int:tache_id>/', editer_tache, name='editer_tache'),
    path('supprimer_tache/<int:tache_id>/', supprimer_tache, name='supprimer_tache'),
]
