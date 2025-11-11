# ============================================================
# 🔹 model_deploy.py — Dashboard Streamlit MLOps Pipeline
# ============================================================

import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
import os
import warnings

warnings.filterwarnings("ignore")

# ============================================================
# Configuración general
# ============================================================

st.set_page_config(
    page_title="Monitoreo de Modelos — Pipeline ML",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard de Monitoreo del Modelo")
st.markdown("### Proyecto Final — Machine Learning (MLOps Pipeline)")

# ============================================================
# Carga de archivos y modelos
# ============================================================

try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = os.getcwd()

base_path = os.path.abspath(os.path.join(base_dir, '../data'))

files = {
    "drift": os.path.join(base_path, 'drift_report.csv'),
    "results": os.path.join(base_path, 'model_results_summary.csv'),
    "logreg": os.path.join(base_path, 'best_model_logreg.pkl'),
    "rf": os.path.join(base_path, 'best_model_rf.pkl'),
    "xgb": os.path.join(base_path, 'best_model_xgb.pkl')
}

missing = [k for k, v in files.items() if not os.path.exists(v)]
if missing:
    st.error(f"❌ Faltan los siguientes archivos: {', '.join(missing)}")
    st.stop()

# Modelos y datos
logreg = joblib.load(files["logreg"])
rf = joblib.load(files["rf"])
xgb = joblib.load(files["xgb"])

df_results = pd.read_csv(files["results"])
df_drift = pd.read_csv(files["drift"])

# ============================================================
# Limpieza y validación de resultados
# ============================================================

df_results.columns = (
    df_results.columns
    .str.strip()
    .str.replace('\n', '')
    .str.replace('\r', '')
    .str.lower()
    .str.replace(' ', '_')
)

df_results.rename(columns={
    'accuracy': 'Accuracy',
    'f1_score': 'F1 Score',
    'modelo': 'Modelo'
}, inplace=True)

st.success("✅ Datos y modelos cargados correctamente.")

# ============================================================
# Comparación de métricas
# ============================================================

st.subheader("📈 Desempeño comparativo de los modelos")

col_model = [c for c in df_results.columns if 'model' in c.lower()][0]
col_acc_test = [c for c in df_results.columns if 'accuracy' in c.lower() and 'test' in c.lower()][0]
col_f1_test = [c for c in df_results.columns if 'f1' in c.lower() and 'test' in c.lower()][0]

col1, col2, col3 = st.columns(3)
col1.metric("Mejor Accuracy (Test)", f"{df_results[col_acc_test].max():.3f}")
col2.metric("Mejor F1 Score (Test)", f"{df_results[col_f1_test].max():.3f}")
col3.metric("Modelos evaluados", f"{len(df_results)}")

st.dataframe(df_results.style.highlight_max(axis=0, color='#A3E4D7'))

# ============================================================
# Visualización comparativa
# ============================================================

st.markdown("### 📊 Visualización de resultados")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

sns.barplot(data=df_results, x=col_model, y=col_acc_test, hue=col_model, legend=False, ax=ax[0], palette="crest")
ax[0].set_title("Accuracy por modelo")
ax[0].set_xlabel("Modelo")
ax[0].set_ylabel("Accuracy (Test)")

sns.barplot(data=df_results, x=col_model, y=col_f1_test, hue=col_model, legend=False, ax=ax[1], palette="flare")
ax[1].set_title("F1 Score por modelo")
ax[1].set_xlabel("Modelo")
ax[1].set_ylabel("F1 Score (Test)")

plt.tight_layout()
st.pyplot(fig)

# ============================================================
# Monitoreo de Drift
# ============================================================

st.subheader("📉 Monitoreo de Drift")

if not df_drift.empty:
    st.dataframe(df_drift.head())
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df_drift, x=df_drift.index, y="Drift", hue=df_drift.index, legend=False, palette="viridis", ax=ax)
    ax.set_title("Magnitud del Drift por variable")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.info("No se detectó Drift en las variables analizadas.")

# ============================================================
# Mejor modelo según F1 Score (Test)
# ============================================================

col_model = [c for c in df_results.columns if 'model' in c.lower()][0]
col_f1_test = [c for c in df_results.columns if 'f1' in c.lower() and 'test' in c.lower()][0]

best_model_row = df_results.loc[df_results[col_f1_test].idxmax()]
best_model = best_model_row[col_model]
best_score = best_model_row[col_f1_test]

st.markdown("---")
st.success(f"🏆 El mejor modelo según **F1 Score (Test)** es **{best_model}** con un puntaje de **{best_score:.3f}**")

# ============================================================
# Predicciones masivas desde la API
# ============================================================

st.subheader("🧩 Resultados de inferencias desde la API")

pred_file = os.path.join(base_path, "predicciones.csv")

if os.path.exists(pred_file):
    df_preds = pd.read_csv(pred_file)
    st.dataframe(df_preds.head(10))

    aprobados = (df_preds["prediccion"] == 1).sum()
    rechazados = (df_preds["prediccion"] == 0).sum()

    st.success(f"✅ Total aprobados: {aprobados} | ❌ Total rechazados: {rechazados}")

    fig, ax = plt.subplots(figsize=(5, 4))
    sns.countplot(x="prediccion", data=df_preds, palette=["#E74C3C", "#27AE60"])
    ax.set_title("Distribución de predicciones")
    ax.set_xticklabels(["Rechazado (0)", "Aprobado (1)"])
    st.pyplot(fig)

else:
    st.warning("⚠️ No se ha encontrado el archivo 'predicciones.csv'. Ejecuta test_request.py para generarlo.")
