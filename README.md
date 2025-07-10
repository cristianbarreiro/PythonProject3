
# Proyecto Python + TensorFlow con Conda

Este repositorio contiene un proyecto base para trabajar con **Python 3.10** y **TensorFlow** dentro de un entorno Conda.

---

## 1. Crear entorno Conda

```bash
conda create -n tf_env310 python=3.10
conda activate tf_env310
```

---

## 2. Instalar paquetes necesarios

```bash
pip install --upgrade pip
pip install tensorflow numpy
```

> ⚠️ Para evitar errores con NumPy y TensorFlow, usa Python 3.10 o 3.11 y versiones compatibles.

---

## 3. Configurar PyCharm

- En **File > Settings > Project: > Python Interpreter**, seleccioná el intérprete de Python del entorno Conda (`tf_env310`).
- Asegurate que el intérprete apunta a algo como:  
  `C:\Users\tu_usuario\anaconda3\envs\tf_env310\python.exe`
- Al ejecutar, PyCharm usará ese entorno con las librerías instaladas.

---

## 4. Manejo de advertencias comunes

TensorFlow puede mostrar advertencias como:

```
oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors...
```

Para desactivar esta advertencia, exportá la variable de entorno antes de ejecutar:

```bash
set TF_ENABLE_ONEDNN_OPTS=0      # Windows CMD
# o en PowerShell:
$env:TF_ENABLE_ONEDNN_OPTS=0
# o en Linux/macOS:
export TF_ENABLE_ONEDNN_OPTS=0
```

---

## 5. Archivo `.gitignore` recomendado

```gitignore
# Python
__pycache__/
*.py[cod]

# Conda environment files
env/
venv/
.tf_env310/

# PyCharm
.idea/
*.iml

# Logs
*.log

# Jupyter
.ipynb_checkpoints

# TensorFlow saved models
saved_model/
```

---

## 6. Archivo `requirements.txt`

```txt
tensorflow>=2.10
numpy>=1.23
```

Instalación desde requirements:

```bash
pip install -r requirements.txt
```

---

## 7. Subir proyecto a GitHub

```bash
git init
git add .
git commit -m "Primer commit"
git remote add origin https://github.com/tu_usuario/tu_repositorio.git
git branch -M main
git push -u origin main
```

Si recibís error por commits remotos:

```bash
git pull --rebase origin main
git push -u origin main
```

---

## 8. Recomendaciones

- Evitá usar Python 3.13 porque algunas librerías (como NumPy) aún no tienen soporte completo.
- Usá entornos Conda para aislar dependencias y evitar conflictos.
- Mantene actualizado pip y las librerías.
- Consultá la [guía oficial de TensorFlow](https://www.tensorflow.org/install) para detalles específicos.

---

¡Listo! Ya tenés un entorno preparado para empezar a aprender y trabajar con TensorFlow sin problemas.

---

Si querés, te ayudo a crear un script de instalación automática o a configurar PyCharm paso a paso.

---

¿Te sirvió? ¿Querés que lo adapte a tu proyecto o que te ayude con algún otro tema?
