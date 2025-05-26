import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import mlflow
import mlflow.sklearn

# Activer le suivi MLflow
mlflow.set_experiment("Cancer_du_sein_RF")

# Lire les données
df = pd.read_csv("data/breast_cancer.csv")

# Nettoyage des colonnes inutiles
df = df.drop(columns=["id", "Unnamed: 32"])

# Conversion de 'diagnosis' en variable cible binaire
df['target'] = df['diagnosis'].map({'M': 1, 'B': 0})

# Supprimer la colonne 'diagnosis' originale
df = df.drop(columns=["diagnosis"])

# Affichage pour vérification
print("Colonnes après nettoyage :", df.columns)
print(df.head())

# Séparation X/y
X = df.drop('target', axis=1)
y = df['target']

# Division en jeu d'entraînement/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparamètres
n_estimators = 100
max_depth = 5
random_state = 42

# Démarrage du tracking MLflow
with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print(classification_report(y_test, y_pred))

    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "random_forest_model")
