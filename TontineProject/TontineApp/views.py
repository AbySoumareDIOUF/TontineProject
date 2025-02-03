from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password  # Pour hacher et vérifier le mot de passe
from .models import Utilisateur, Statut
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.utils import timezone

def index(request):
    context = {}
    return render(request, 'Index.html', context)

def Connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mdp = request.POST.get('mdp')

        try:
            utilisateur = Utilisateur.objects.get(email=email)
            
            # Vérification du mot de passe (hachage sécurisé avec check_password)
            if check_password(mdp, utilisateur.mdp):  # compare le mot de passe en texte clair avec le mot de passe haché
                utilisateur.last_login = timezone.now()  # Mise à jour du champ last_login
                utilisateur.save()

                # Connexion réussie, redirection vers la page d'accueil ou autre
                return redirect('index')

            else:
                messages.error(request, "Email ou mot de passe incorrect.")
        except Utilisateur.DoesNotExist:
            messages.error(request, "Utilisateur non trouvé.")
    
    return render(request, 'Connexion.html')

def inscription(request):
    return render(request, "inscription.html")

def register(request):
    if request.method == 'POST':
        # Récupération des données
        nom = request.POST.get('nom')
        prenoms = request.POST.get('prenoms')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        ville = request.POST.get('ville')
        cni = request.FILES.get('cni')  # Récupérer le fichier image de la carte d'identité
        mdp = request.POST.get('mdp')
        mdp_confirm = request.POST.get('mdp_confirm')

        # Vérification que les mots de passe correspondent
        if mdp != mdp_confirm:
            return render(request, 'inscription.html', {'error': 'Les mots de passe ne correspondent pas.'})

        # Vérification que les champs obligatoires sont remplis
        if not nom or not prenoms or not email or not telephone or not ville or not cni or not mdp:
            return render(request, 'inscription.html', {'error': 'Tous les champs doivent être remplis.'})

        # Récupérer le statut 'user' par défaut
        statut_user = Statut.objects.get(libelle='user')

        # Hachage du mot de passe
        mdp_hache = make_password(mdp)

        # Enregistrer les données dans la base
        utilisateur = Utilisateur(
            statut=statut_user,  # Assigner le statut 'user'
            nom=nom,
            prenoms=prenoms,
            email=email,
            telephone=telephone,
            ville=ville,
            cni=cni,
            mdp=mdp_hache,  # Enregistrer le mot de passe haché
        )
        
        try:
            utilisateur.save()  # Sauvegarde dans la base de données
            return redirect('Connexion')  # Rediriger vers la page de connexion après inscription réussie
        except ValidationError as e:
            return render(request, 'inscription.html', {'error': str(e)})

    return render(request, 'inscription.html')
