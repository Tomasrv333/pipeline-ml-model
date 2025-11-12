
# 🧠 MLOps Pipeline — Proyecto Final de Machine Learning

Este proyecto implementa una **pipeline completa de Machine Learning bajo principios MLOps**, abarcando desde la **carga y exploración de datos** hasta el **entrenamiento, evaluación, despliegue y monitoreo** de los modelos.  
El desarrollo forma parte del **Proyecto Final de la asignatura Machine Learning** de la **Luis Amigo** (2025).

---

## 📦 Estructura General del Proyecto

```
MACHINE-LEARNING/
│
├── data/
│   ├── Base_de_datos.csv                # Dataset principal del proyecto
│
├── mlops_pipeline/
│   ├── data/
│   │   ├── drift_report.csv             # Reporte de drift detectado
│   │   ├── model_results_summary.csv    # Resultados comparativos de modelos
│   │   ├── predicciones.csv             # Predicciones masivas generadas desde la API
│   │
│   └── src/
│       ├── Cargar_datos.ipynb           # Limpieza y carga inicial del dataset
│       ├── comprension_eda.ipynb        # Exploración de datos (EDA)
│       ├── ft_engineering.ipynb         # Ingeniería de características
│       ├── heuristic_model.py           # Modelo base heurístico
│       ├── model_training.ipynb         # Entrenamiento de modelos ML
│       ├── model_evaluation.ipynb       # Evaluación y métricas de desempeño
│       ├── model_monitoring.ipynb       # Detección de drift y monitoreo
│       ├── api_deploy.py                # API de predicción (FastAPI)
│       ├── test_request.py              # Pruebas masivas de la API
│       ├── model_deploy.py              # Dashboard de monitoreo (Streamlit)
│
├── mlops_pipeline-venv/                 # Entorno virtual del proyecto
│
├── Dockerfile.api                       # Imagen Docker para la API
├── Dockerfile.dashboard                 # Imagen Docker para el dashboard
├── docker-compose.yml                   # Orquestador de API + Dashboard
├── config.json                          # Configuración global
├── requirements.txt                     # Dependencias del proyecto
├── set_up.bat                           # Script automático de instalación
└── readme.md                            # Documentación del proyecto
```

---

## 🎯 Objetivo General

Desarrollar una **pipeline de Machine Learning automatizada y reproducible**, enfocada en:

- 🔁 Automatizar el ciclo de vida del modelo.  
- 🧩 Integrar buenas prácticas de **MLOps**.  
- 🚀 Desplegar el modelo de forma funcional mediante **FastAPI**.  
- 📊 Monitorear el rendimiento con **Streamlit**.  
- ⚙️ Facilitar la ejecución mediante **entorno virtual y contenedores Docker**.

---

## ⚙️ Instalación y Ejecución

### 1️⃣ Instalación automática (recomendada)
Ejecuta el script incluido para preparar el entorno de trabajo:
```bash
set_up.bat
```

Este script:
- Crea el entorno virtual `mlops_pipeline-venv`.
- Instala automáticamente todas las dependencias.
- Configura las rutas necesarias para ejecutar los notebooks y scripts.

---

### 2️⃣ Activación manual del entorno (si prefieres hacerlo tú)

```bash
mlops_pipeline-venv\Scripts\activate
```

---

### 3️⃣ Despliegue del modelo vía API

```bash
python mlops_pipeline/src/api_deploy.py
```

La API se levantará en:
👉 [http://localhost:8000](http://localhost:8000)

#### Endpoints disponibles:
- `/` → Estado de la API.  
- `/predict` → Endpoint de inferencia (acepta datos JSON).

#### Ejemplo de solicitud:
```json
[
  {
    "edad": 35,
    "ingresos": 2500000,
    "duracion_prestamo": 24,
    "genero": "M",
    "tipo_empleo": "Empleado"
  }
]
```

#### Ejemplo de respuesta:
```json
{
  "predicciones": [1],
  "total_registros": 1,
  "timestamp": "2025-11-11T18:42:15"
}
```
> **1 = Aprobado**  
> **0 = Rechazado**

---

### 4️⃣ Pruebas masivas (Test Request)

```bash
python mlops_pipeline/src/test_request.py
```

📁 Genera un archivo `predicciones.csv` en `mlops_pipeline/data/`, con resultados de inferencias masivas.

---

### 5️⃣ Dashboard de Monitoreo (Streamlit)

```bash
streamlit run mlops_pipeline/src/model_deploy.py
```

🌐 Abre automáticamente en:
[http://localhost:8501](http://localhost:8501)

Incluye:
- Comparativa de métricas (Accuracy, F1).  
- Mejor modelo detectado automáticamente.  
- Visualización del **Drift** entre datasets.  
- Panel de predicciones masivas integradas desde la API.

---

## 📊 Cumplimiento de la Rúbrica de Evaluación

| Criterio | Descripción | Cumple |
|:--|:--|:--:|
| **Preprocesamiento** | Limpieza y validación de datos | ✅ |
| **EDA** | Exploración con visualizaciones y estadísticos | ✅ |
| **Feature Engineering** | Transformaciones aplicadas correctamente | ✅ |
| **Entrenamiento y Validación** | Múltiples modelos comparados | ✅ |
| **Evaluación** | Métricas completas y análisis visual | ✅ |
| **Despliegue API** | FastAPI funcional y probada | ✅ |
| **Monitoreo** | Drift reportado y visualizado | ✅ |
| **Dashboard** | Streamlit con métricas integradas | ✅ |
| **Contenerización** | Dockerfile + Compose funcionales | ✅ |
| **Documentación** | README completo y estructurado | ✅ |

---

## 👨‍💻 Autor

**Tomás Ríos Vargas**  
Ingeniería de Sistemas  
📍 Medellín, Colombia  
✉️ [tomas.riosva@amigo.edu.co](mailto:tomas.riosva@amigo.edu.co)  
📘 Universidad Luis Amigo — Proyecto Final de Machine Learning  

---

## 🧾 Licencia

Este proyecto es de uso **académico y educativo**.  
© 2025 — Todos los derechos reservados.
