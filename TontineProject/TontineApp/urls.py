from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inscription/', views.inscription, name='inscription'),
    path('Connexion/', views.Connexion, name='Connexion'),
    path('register/', views.register, name='register'),  # Ajoute cette ligne pour gérer le POST du formulaire d'inscription
]

# Assure-toi que les fichiers médias sont correctement servis en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
