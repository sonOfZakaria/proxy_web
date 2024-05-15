# Utiliser une image de base Python officielle
FROM python:2.7-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du code source de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel le serveur proxy écoutera
EXPOSE 9999

# Commande pour démarrer l'application quand le conteneur est lancé
CMD ["python", "projet.py"]