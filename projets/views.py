# projets/views.py
from django.shortcuts import render, redirect
from .models import Projet, Tache
from .forms import ProjetForm, TacheForm  # Nous allons créer ces formulaires

def liste_projets(request):
    projets = Projet.objects.all()
    return render(request, 'projets/liste_projets.html', {'projets': projets})

def creer_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.utilisateur = request.user.profil  # Assurez-vous que l'utilisateur est authentifié
            projet.save()
            return redirect('liste_projets')
    else:
        form = ProjetForm()
    return render(request, 'projets/creer_projet.html', {'form': form})

def creer_tache(request, projet_id):
    projet = Projet.objects.get(id=projet_id)
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.projet = projet
            tache.save()
            return redirect('liste_projets')
    else:
        form = TacheForm()
    return render(request, 'projets/creer_tache.html', {'form': form, 'projet': projet})
