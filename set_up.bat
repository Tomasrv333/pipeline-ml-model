@echo off
setlocal EnableDelayedExpansion

REM ===========================================
REM   Script: set_up.bat
REM   Autor:  Tomás Ríos
REM   Propósito: Configurar entorno virtual para MLOps Pipeline
REM   Versión estable 2025-11
REM ===========================================

echo.
echo === INICIO DE CONFIGURACIÓN DEL ENTORNO ===
echo.

REM Obtener la ruta absoluta del directorio del script
set "SCRIPT_DIR=%~dp0"
echo Directorio actual del script: %SCRIPT_DIR%

REM Movernos al directorio del script por seguridad
cd /d "%SCRIPT_DIR%"

REM ================================
REM Buscar y leer el project_code en config.json
REM ================================
if exist "%SCRIPT_DIR%config.json" (
    for /f "usebackq tokens=2 delims=:" %%A in (`findstr "project_code" "%SCRIPT_DIR%config.json"`) do (
        set "line=%%A"
        set "line=!line:,=!"
        set "line=!line:"=!"
        set "project_code=!line:~1!"
    )
) else (
    echo ❌ No se encontró config.json en %SCRIPT_DIR%.
    pause
    exit /b 1
)

if not defined project_code (
    set "project_code=mlops_pipeline"
    echo ⚠️ No se encontró project_code en config.json. Se usará nombre por defecto: mlops_pipeline
)

echo Nombre del proyecto detectado: %project_code%
echo.

REM ================================
REM Crear entorno virtual dentro del proyecto
REM ================================
set "venv_path=%SCRIPT_DIR%%project_code%-venv"
if exist "%venv_path%" (
    echo ⚠️ El entorno virtual ya existe en: %venv_path%
) else (
    echo Creando entorno virtual en: %venv_path%
    py -m venv "%venv_path%"
)

REM ================================
REM Activar el entorno virtual
REM ================================
echo.
echo Activando entorno virtual...
call "%venv_path%\Scripts\activate"

if %ERRORLEVEL% NEQ 0 (
    echo ❌ Error activando el entorno virtual.
    pause
    exit /b 1
)

echo ✅ Entorno activado correctamente.
echo Python actual:
where python
echo.

REM ================================
REM Instalar dependencias
REM ================================
echo === Instalando librerías de requirements.txt ===
if exist "%SCRIPT_DIR%requirements.txt" (
    pip install --no-cache-dir -r "%SCRIPT_DIR%requirements.txt"
    if %ERRORLEVEL% EQU 0 (
        echo ✅ Todas las librerías se instalaron correctamente.
    ) else (
        echo ❌ Error al instalar librerías.
        pause
        exit /b 1
    )
) else (
    echo ⚠️ No se encontró requirements.txt en: %SCRIPT_DIR%
)

REM ================================
REM Registrar kernel en Jupyter
REM ================================
echo.
echo === Registrando entorno virtual con Jupyter ===
python -m ipykernel install --user --name=%project_code%-venv --display-name "%project_code%-venv Python ETL"

if %ERRORLEVEL% EQU 0 (
    echo ✅ Kernel registrado correctamente. 
    echo Selecciona "%project_code%-venv Python ETL" en Jupyter Notebook o VSCode.
) else (
    echo ⚠️ No se pudo registrar el kernel en Jupyter.
)

echo.
echo === CONFIGURACIÓN COMPLETA ===
pause
