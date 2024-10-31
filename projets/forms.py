# projets/forms.py
from django import forms
from .models import Projet, Tache

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['titre', 'description']

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description']
