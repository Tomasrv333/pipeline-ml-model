# ============================================================
# 🔹 api_deploy.py — Servicio de inferencia del modelo
# ============================================================

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from typing import List
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
import datetime as dt

app = FastAPI(
    title="API de Predicción — Proyecto Machine Learning",
    description="Servicio de inferencia del mejor modelo entrenado (MLOps Pipeline)",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta base
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data"))

model_path = os.path.join(base_path, "best_model_xgb.pkl")
preproc_path = os.path.join(base_path, "preprocessor.pkl")

model = joblib.load(model_path)
preprocessor = joblib.load(preproc_path)

# ============================================================
# 1️⃣ Esquema de entrada (alineado con el training)
# ============================================================

class InputData(BaseModel):
    income: float
    credit_score: float
    loan_amount: float
    years_employed: float
    points: float

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "income": 60000,
                    "credit_score": 700,
                    "loan_amount": 20000,
                    "years_employed": 5,
                    "points": 55,
                }
            ]
        }
    )

# ============================================================
# 2️⃣ Endpoints
# ============================================================

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "API de predicción activa 🚀",
        "timestamp": dt.datetime.now().isoformat()
    }

@app.post("/predict")
def predict(input_data: List[InputData]):
    # DataFrame con las mismas columnas que el modelo espera
    df_raw = pd.DataFrame([item.dict() for item in input_data])

    # Aplicar el mismo preprocesamiento que en entrenamiento
    X_new = preprocessor.transform(df_raw)

    # Predicciones
    preds = model.predict(X_new)

    return {
        "predicciones": preds.tolist(),
        "total_registros": len(preds),
        "timestamp": dt.datetime.now().isoformat()
    }

if __name__ == "__main__":
    uvicorn.run("api_deploy:app", host="0.0.0.0", port=8000, reload=True)
