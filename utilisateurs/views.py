from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UtilisateurInscriptionForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


def inscription(request):
    if request.method == "POST":
        form = UtilisateurInscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après l'inscription
            return redirect('utilisateurs:connexion')  
    else:
        form = UtilisateurInscriptionForm()
    return render(request, 'utilisateurs/inscription.html', {'form': form})

class UtilisateurConnexionView(LoginView):
    template_name = 'utilisateurs/connexion.html'


class UtilisateurDeconnexionView(LogoutView):
    next_page = 'home'

def home(request):
    return render(request, 'home.html')