# projets/views.py
from django.shortcuts import render, redirect ,get_object_or_404
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

def editer_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('liste_projets')
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'projets/editer_projet.html', {'form': form, 'projet': projet})


# suppression projet 
def supprimer_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        projet.delete()
        return redirect('liste_projets')
    return render(request, 'projets/supprimer_projet.html', {'projet': projet})

# Edit tache 
def editer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=tache)
        if form.is_valid():
            form.save()
            return redirect('liste_projets')
    else:
        form = TacheForm(instance=tache)
    return render(request, 'projets/editer_tache.html', {'form': form, 'tache': tache})


# delete tache
def supprimer_tache(request, tache_id):
    tache = get_object_or_404(Tache, id=tache_id)
    if request.method == 'POST':
        tache.delete()
        return redirect('liste_projets')
    return render(request, 'projets/supprimer_tache.html', {'tache': tache})
