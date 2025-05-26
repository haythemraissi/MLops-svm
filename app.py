import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd
from logstash_formatter import LogstashFormatterV1

# Configuration du logger
logger = logging.getLogger("ml_project_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/ml_project.log")  # Le fichier log sera lu par Logstash
file_handler.setFormatter(LogstashFormatterV1())  # Format JSON

logger.addHandler(file_handler)

# Définir la structure des données d'entrée
class InputData(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float
    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float

# Initialisation de FastAPI
app = FastAPI()

# Charger le modèle MLflow
try:
    model_path = "mlruns/749469777560196776/a14067c71f804e389bccdc706448d7ec/artifacts/random_forest_model"
    model = mlflow.pyfunc.load_model(model_path)
    logger.info("Modèle MLflow chargé avec succès.")
except Exception as e:
    logger.error("Erreur lors du chargement du modèle MLflow", exc_info=True)
    raise RuntimeError("Erreur lors du chargement du modèle MLflow.")

@app.get("/")
def root():
    logger.info("GET / appelé")
    return {"message": "API FastAPI pour prédiction cancer du sein"}

@app.post("/predict")
def predict(data: InputData):
    try:
        logger.info("POST /predict appelé", extra={"input_data": data.dict()})
        df = pd.DataFrame([data.dict()])

        # Renommage des colonnes pour correspondre aux noms du modèle
        df = df.rename(columns={
            'concave_points_mean': 'concave points_mean',
            'concave_points_se': 'concave points_se',
            'concave_points_worst': 'concave points_worst'
        })

        prediction = model.predict(df)
        result = int(prediction[0])
        logger.info("Résultat de prédiction", extra={"prediction": result})
        return {"prediction": result}
    except Exception as e:
        logger.error("Erreur pendant la prédiction", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
