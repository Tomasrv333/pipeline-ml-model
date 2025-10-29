# 🧠 MLOps Pipeline – Proyecto de Machine Learning

Este proyecto implementa una **pipeline de Machine Learning completa** —desde la carga y exploración de datos hasta el despliegue, evaluación y monitoreo del modelo—, como parte de la asignatura de **Machine Learning**.

---

## 📁 Estructura del Proyecto

```
MACHINE-LEARNING/
│
├── mlops_pipeline/
│   └── src/
│       ├── Cargar_datos.ipynb         # Carga y preprocesamiento inicial de los datos
│       ├── comprension_eda.ipynb      # Análisis exploratorio de datos (EDA)
│       ├── ft_engineering.py          # Ingeniería de características
│       ├── heuristic_model.py         # Modelo base o heurístico para comparación
│       ├── model_training.ipynb       # Entrenamiento del modelo
│       ├── model_evaluation.ipynb     # Evaluación y métricas del modelo
│       ├── model_deploy.ipynb         # Despliegue del modelo
│       ├── model_monitoring.ipynb     # Monitoreo del modelo en producción
│
├── Base_de_datos.csv                  # Fuente principal de datos
├── config.json                        # Configuraciones globales del proyecto
├── requirements.txt                   # Librerías necesarias
├── set_up.bat                         # Script para entorno de ejecución en Windows
├── readme.md                          # Este archivo :)
```

---

## 🚀 Objetivo del Proyecto

El propósito de esta pipeline es **automatizar el ciclo de vida de un modelo de Machine Learning**, siguiendo los principios de **MLOps**, para garantizar reproducibilidad, mantenibilidad y monitoreo continuo.

### Etapas principales:
1. **Carga de datos:** Importación y limpieza de datos.
2. **Exploración (EDA):** Visualización y comprensión de patrones.
3. **Ingeniería de características:** Creación y transformación de variables.
4. **Modelado:** Entrenamiento y validación de modelos.
5. **Evaluación:** Comparación de métricas y ajuste fino.
6. **Despliegue:** Exportación del modelo para uso en producción.
7. **Monitoreo:** Seguimiento del rendimiento del modelo en tiempo real.

---

## ⚙️ Instalación y Uso

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/usuario/mlops_pipeline.git
cd mlops_pipeline
```

### 2️⃣ Crear entorno virtual (opcional)
```bash
python -m venv venv
venv\Scripts\activate    # En Windows
source venv/bin/activate   # En Linux/Mac
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar el entorno de notebooks
```bash
jupyter notebook
```

---

## 🧩 Archivos clave

| Archivo | Descripción |
|----------|--------------|
| **Cargar_datos.ipynb** | Limpieza y preparación inicial de datos |
| **comprension_eda.ipynb** | Análisis exploratorio y visualización |
| **ft_engineering.py** | Generación de nuevas variables |
| **heuristic_model.py** | Modelo base para referencia |
| **model_training.ipynb** | Entrenamiento del modelo final |
| **model_evaluation.ipynb** | Evaluación cuantitativa y cualitativa |
| **model_deploy.ipynb** | Despliegue del modelo entrenado |
| **model_monitoring.ipynb** | Seguimiento del rendimiento del modelo |
| **Base_de_datos.csv** | Dataset principal utilizado |
| **config.json** | Parámetros de configuración del proyecto |
| **requirements.txt** | Librerías necesarias |
| **set_up.bat** | Script de configuración automática en Windows |

---

## 🧪 Tecnologías Utilizadas

- 🐍 **Python 3.10+**
- 📊 **Pandas**, **NumPy**
- 🤖 **Scikit-learn**
- 📈 **Matplotlib**, **Seaborn**
- 🧱 **Jupyter Notebook**
- 🧰 **MLOps Tools** (para despliegue y monitoreo)

---

## 📉 Resultados Esperados

- Un modelo entrenado y desplegado con rendimiento medible.  
- Un flujo reproducible que permita entrenar, evaluar y monitorear nuevos modelos fácilmente.  
- Un entendimiento profundo del **pipeline MLOps** aplicado a Machine Learning.

---

## 👨‍💻 Autor

**Tomás Ríos Vargas**  
Estudiante de Ingeniería de Sistemas  
📍 Medellín, Colombia  
✉️ [tomas.riosva@amigo.edu.co](mailto:tomas.riosva@amigo.edu.co)

---

## 🧾 Licencia

Este proyecto es de uso académico y educativo.  
© 2025 – Todos los derechos reservados.
