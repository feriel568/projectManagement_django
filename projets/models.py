# projets/models.py
from django.db import models
from utilisateurs.models import Profil  # Assurez-vous que le modèle Profil existe

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(Profil, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

class Tache(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='taches')
    date_creation = models.DateTimeField(auto_now_add=True)
    est_terminee = models.BooleanField(default=False)

    def __str__(self):
        return self.titre
