# ============================================================
# 🔹 heuristic_model.py — Modelo base (baseline)
# ============================================================

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

# Cargar datos ya separados
y_train = np.load('../data/y_train.npy', allow_pickle=True)
y_test = np.load('../data/y_test.npy', allow_pickle=True)

# ============================================================
# 🔸 Regla heurística: predecir siempre la clase mayoritaria
# ============================================================
print("Forma de y_train:", y_train.shape)
most_frequent = np.bincount(y_train.astype(int).ravel()).argmax()
y_pred_baseline = np.full_like(y_test, fill_value=most_frequent)

# ============================================================
# 🔸 Métricas básicas
# ============================================================
acc = accuracy_score(y_test, y_pred_baseline)
f1 = f1_score(y_test, y_pred_baseline)
cm = confusion_matrix(y_test, y_pred_baseline)

print("Modelo heurístico (baseline):")
print(f"Predice siempre la clase: {most_frequent}")
print(f"Accuracy: {acc:.3f}")
print(f"F1 Score: {f1:.3f}")
print("Matriz de confusión:")
print(cm)
