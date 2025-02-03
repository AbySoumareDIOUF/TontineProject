from django.db import models
from django.utils import timezone
# Statut
class Statut(models.Model):
    libelle = models.CharField(max_length=50)

    def __str__(self):
        return self.libelle

# Utilisateur

class Utilisateur(models.Model):
    statut = models.ForeignKey(Statut, on_delete=models.CASCADE, related_name='services')
    nom = models.CharField(max_length=50)
    prenoms = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    cni = models.ImageField(upload_to='cni/', max_length=100)
    telephone = models.CharField(max_length=15)
    ville = models.TextField()
    mdp = models.CharField(max_length=255)
    
    # Ajout du champ last_login
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenoms}"
