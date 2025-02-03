# Utilise une image Python officielle comme base
FROM python:3.9-slim

# Installer les dépendances système nécessaires pour mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Crée un répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app/

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port sur lequel l'application Django fonctionnera
EXPOSE 8000

# Lancer le serveur Django en mode production (utilise Gunicorn ou autre serveur WSGI)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "TontineProject.wsgi:application"]
