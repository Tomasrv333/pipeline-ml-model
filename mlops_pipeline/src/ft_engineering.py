# ============================================================
# 🔹 ft_engineering.py — Ingeniería de características
# ============================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# ============================================================
# 🔸 1. Cargar datasets preparados por el EDA
# ============================================================
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))

X_path = os.path.join(base_path, 'Base_de_datos_sin_target.csv')
y_path = os.path.join(base_path, 'Target_loan_approved.csv')

X = pd.read_csv(X_path)
y = pd.read_csv(y_path)

# 🔧 Convertir a vector 1D
if 'loan_approved' in y.columns:
    y = y['loan_approved']

# Convertir booleanos a enteros
y = y.astype(int)

print("✅ Datos cargados correctamente.")
print(f"Dimensiones de X: {X.shape}")
print(f"Dimensiones de y: {y.shape}")

# ============================================================
# 🔸 2. Identificar tipos de columnas
# ============================================================
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = X.select_dtypes(include=['object']).columns.tolist()

print("Columnas numéricas:", numeric_features)
print("Columnas categóricas:", categorical_features)

# ============================================================
# 🔸 3. Definir transformadores
# ============================================================
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# ============================================================
# 🔸 4. Crear preprocesador
# ============================================================
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# ============================================================
# 🔸 5. Aplicar transformación y crear splits
# ============================================================
X = X.reset_index(drop=True)
y = y.reset_index(drop=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Conjuntos creados:")
print(f" - Entrenamiento: {X_train.shape}")
print(f" - Prueba: {X_test.shape}")

# Ajustar transformador al entrenamiento
preprocessor.fit(X_train)

# Transformar datos (manejo flexible si no hay variables categóricas)
X_train_transformed = preprocessor.fit_transform(X_train)
X_test_transformed = preprocessor.transform(X_test)

# Si el resultado es una matriz dispersa (de OneHotEncoder), conviértela
if not isinstance(X_train_transformed, np.ndarray):
    X_train_transformed = X_train_transformed.toarray()
    X_test_transformed = X_test_transformed.toarray()


print("✅ Transformaciones aplicadas correctamente.")

# ============================================================
# 🔸 6. Guardar conjuntos procesados y el pipeline
# ============================================================

# Guardar arrays procesados
np.save(os.path.join(base_path, 'X_train.npy'), X_train_transformed)
np.save(os.path.join(base_path, 'X_test.npy'), X_test_transformed)
np.save(os.path.join(base_path, 'y_train.npy'), y_train.to_numpy())
np.save(os.path.join(base_path, 'y_test.npy'), y_test.to_numpy())

# Guardar pipeline
joblib.dump(preprocessor, os.path.join(base_path, 'preprocessor.pkl'))

print("✅ Archivos exportados:")
print(" - X_train.npy, X_test.npy, y_train.npy, y_test.npy")
print(" - preprocessor.pkl")

# ============================================================
# 🔸 7. Reporte final
# ============================================================
print("\n📋 Resumen del proceso de ingeniería de características:")
print("------------------------------------------------------------")
print(f"Columnas numéricas escaladas: {numeric_features}")
print(f"Columnas categóricas codificadas: {categorical_features}")
print("Pipeline completo guardado para uso en entrenamiento.")
