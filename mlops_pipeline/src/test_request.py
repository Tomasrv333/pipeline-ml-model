import requests
import pandas as pd
import random

API_URL = "http://127.0.0.1:8000/predict"

def generar_datos(n=1000):
    data = []
    for _ in range(n):
        registro = {
            "income": random.randint(20000, 150000),          # similar a tu dataset
            "credit_score": random.randint(300, 850),
            "loan_amount": random.randint(5000, 60000),
            "years_employed": random.randint(0, 30),
            "points": random.randint(0, 100),
        }
        data.append(registro)
    return data

data = generar_datos(1000)
response = requests.post(API_URL, json=data)

if response.status_code == 200:
    result = response.json()
    print("✅ Petición exitosa.")
    print(f"Predicciones recibidas: {len(result['predicciones'])}")

    df = pd.DataFrame(data)
    df["prediccion"] = result["predicciones"]
    df.to_csv("../data/predicciones.csv", index=False, encoding="utf-8-sig")

    print("📁 Archivo 'predicciones.csv' generado correctamente.")
    print("Resumen:")
    print(df["prediccion"].value_counts())
else:
    print("❌ Error:", response.status_code, response.text)
