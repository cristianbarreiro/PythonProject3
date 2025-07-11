# TensorFlow + Conda + PyCharm Setup Guide

Este README te guiará paso a paso para configurar un entorno de desarrollo con TensorFlow usando **Anaconda**, **PyCharm** y **Git**. Es ideal para entornos CPU y GPU.

---

## 📦 Requisitos Previos

- Conocimientos básicos de Python.
- Tener instalado:
  - [Anaconda](https://www.anaconda.com/products/distribution)
  - [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/)
  - Git (opcional pero recomendado)
  - Drivers NVIDIA (para usar GPU)

---

## 🔁 Alternativa sin instalación

Si no querés instalar nada aún:
- Usá Google Colab: https://colab.research.google.com/
- Soporta TensorFlow preinstalado.

```python
import tensorflow as tf
print(tf.__version__)
```

---

## 🧠 Crear entorno Conda con TensorFlow

### ▶️ Opción 1: Con soporte GPU

```bash
conda create --name tf_env tensorflow-gpu
conda activate tf_env
```

Ventajas:
- Instala automáticamente CUDA y cuDNN compatibles.

Nota: Las versiones de TensorFlow en conda suelen estar algo desactualizadas.

### ▶️ Opción 2: CPU

```bash
conda create --name tf_env_cpu python=3.10
conda activate tf_env_cpu
conda install pip
pip install tensorflow
```

### ▶️ Generar archivo `requirements.txt`

Una vez configurado:

```bash
pip freeze > requirements.txt
```

Y para instalar en otro entorno:

```bash
pip install -r requirements.txt
```

---

## 💻 Configuración de PyCharm

1. Abrí PyCharm y creá un nuevo proyecto.
2. Seleccioná: `Conda Environment > Existing Environment`
3. Buscá el ejecutable del entorno:

```
C:/Users/TU_USUARIO/anaconda3/envs/tf_env/python.exe
```

4. Activá "Make available to all projects".
5. Comprobá que funcione con:

```python
import tensorflow as tf
print(tf.__version__)
```

---

## 🧯 Solución de errores comunes

### ⚠️ `mkl-service` warning
```bash
pip install mkl-service
```

### ⚠️ `collections.Callable` AttributeError

Actualizar `pyreadline` o eliminarlo:
```bash
pip uninstall pyreadline
pip install pyreadline3
```

### ⚠️ `No module named 'numpy.core._multiarray_umath'`
Reinstalar NumPy compatible:
```bash
pip uninstall numpy
pip install numpy==1.23.5
```

---

## 🚀 Comandos útiles de Git

```bash
# Iniciar repo
git init

# Añadir remote (una sola vez)
git remote add origin https://github.com/usuario/repositorio.git

# Subir rama main
git branch -M main
git push -u origin main
```

---

## 📁 .gitignore recomendado

```gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/
*.env

# IDE
.idea/
.vscode/

# Conda
.conda/
env/
*.log

# OS
.DS_Store
Thumbs.db
```

---

## 📌 Notas

- Tutorial basado en: [TensorFlow Setup Tutorial - YouTube](https://www.youtube.com/watch?v=5Ym-dOS9ssA)
- Compatible con Python 3.10 y TensorFlow 2.12+
- Plataforma: Windows 10+

---

## 🧪 Test de entorno

```bash
conda activate tf_env
python -c "import tensorflow as tf; print(tf.__version__)"
```

---

¡Listo! Ya podés empezar tus proyectos de Deep Learning con TensorFlow. 🚀