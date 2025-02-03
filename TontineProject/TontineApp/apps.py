from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class TontineappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TontineApp'

    def ready(self):
        from .models import Statut  # Déplacer l'import ici pour éviter l'erreur

        def insert_default_statuts(sender, **kwargs):
            # Insérer les valeurs par défaut si elles n'existent pas déjà
            if not Statut.objects.filter(libelle="user").exists():
                Statut.objects.create(libelle="user")
            if not Statut.objects.filter(libelle="admin").exists():
                Statut.objects.create(libelle="admin")

        # Connecter le signal post_migrate pour insérer les valeurs par défaut
        post_migrate.connect(insert_default_statuts, sender=self)
