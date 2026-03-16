# --- À METTRE TOUT EN HAUT DU FICHIER ---
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# --- À METTRE À LA FIN DU FICHIER ---

# 1. INSCRIPTION (Register)
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirige vers la connexion après inscription
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# 2. CONNEXION (Login)
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index') # Redirige vers l'accueil après connexion
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 3. DÉCONNEXION (Logout)
def logout_user(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render

# Vue pour afficher la page d'accueil avec le formulaire
def index(request):
    return render(request, 'index.html')

# Vue pour traiter le texte et compter les mots
def counter(request):
    # On récupère le texte envoyé par le formulaire HTML
    texte = request.POST.get('texte_utilisateur', '') 
    # On compte le nombre de mots
    nombre_de_mots = len(texte.split()) 
    
    # On envoie le résultat à la page HTML suivante
    return render(request, 'counter.html', {'nombre': nombre_de_mots})