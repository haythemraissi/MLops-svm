# Makefile - CI/CD pour projet ML

VENV := venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# Crée et active l'environnement virtuel
venv:
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt

# Lancer le script principal
run:
	$(PYTHON) main.py

# Nettoyer les fichiers générés
clean:
	rm -rf __pycache__ */__pycache__ *.pkl *.png logs/

# Réentraîner le modèle
train:
	$(PYTHON) models/model.py

# Prédire (exécute predict.py avec les paramètres par défaut)
predict:
	$(PYTHON) models/predict.py

# Linting (code quality)
lint:
	flake8 .

# Visualiser les résultats
viz:
	$(PYTHON) utils/visualization.py

# Réexécuter tout le projet (end-to-end)
all: clean venv run
