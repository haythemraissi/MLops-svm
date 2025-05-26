# Utiliser une image officielle Python légère
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt (liste des dépendances)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code dans le conteneur
COPY . .

# Exposer le port 8000 (celui utilisé par uvicorn)
EXPOSE 8000
RUN python -m pip install --upgrade pip

# Commande pour lancer l'API avec reload désactivé (reload = dev uniquement)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
