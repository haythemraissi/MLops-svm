# ♻️ ML Project with FastAPI, MLflow, Docker, and ELK

Ce projet est un pipeline de machine learning complet intégrant les bonnes pratiques **MLOps** : modularisation, traçabilité, API REST, conteneurisation et monitoring.

---

## 📁 Structure du projet

```bash
ml_project/
├── app.py                     # API FastAPI
├── Dockerfile                 # Image Docker de l'API
├── docker-compose.yml         # Orchestration des services
├── requirements.txt           # Dépendances Python
├── mlruns/                    # Logs MLflow
├── models/                    # Modèles sauvegardés
├── notebooks/                 # Analyse exploratoire / entraînement
└── ...
```

---

## 🚀 Fonctionnalités

- 📦 **Modèle ML** : entraînement, prédiction, évaluation
- 🌐 **FastAPI** : API pour exposer le modèle
- 📊 **MLflow** : suivi des expérimentations
- 🐳 **Docker** : conteneurisation de l’API
- 🔍 **Elasticsearch + Kibana** : logs centralisés pour observabilité

---

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone https://github.com/haythemraissi/MLops-svm.git
cd ml_project
```

### 2. Lancer les services Docker

```bash
docker-compose up --build
```

### 3. Accéder aux interfaces

| Service       | URL                         |
|---------------|-----------------------------|
| API FastAPI   | http://localhost:8000       |
| MLflow UI     | http://localhost:5000       |
| Kibana        | http://localhost:5601       |

---

## 🧪 Tester l’API

### Endpoint de prédiction :

```bash
POST http://localhost:8000/predict
Content-Type: application/json

{
  "feature1": 3.2,
  "feature2": 1.5,
  ...
}
```

Réponse :

```json
{
  "prediction": "Classe A"
}
```

---

## 🔍 Monitoring

- **Logs applicatifs** sont envoyés vers **Elasticsearch**
- **Kibana** permet de visualiser en temps réel les requêtes, erreurs, etc.

---

## 📦 Dépendances principales

- Python 3.10
- FastAPI
- Uvicorn
- Scikit-learn
- MLflow
- Docker / Docker Compose
- Elasticsearch / Kibana
- logstash-formatter

---

## 🛠️ Développement local

Créer un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows
pip install -r requirements.txt
```

Lancer l'API localement :

```bash
uvicorn app:app --reload
```

---

## 👤 Auteur

- **Nom** : Haythem Raissi
- **GitHub** : [@haythemraissi](https://github.com/haythemraissi/)

---

## 📄 Licence

Ce projet est sous licence MIT.

