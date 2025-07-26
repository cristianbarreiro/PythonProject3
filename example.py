import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # 👈 Forzar uso de CPU
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'   # Suprimir logs de TF

import warnings
warnings.filterwarnings('ignore', category=UserWarning)

# Redirección avanzada para ocultar "WARNING:tensorflow" en stderr
import sys
import io

class FilteredStderr(io.StringIO):
    def write(self, s):
        if "WARNING:tensorflow" not in s:
            sys.__stderr__.write(s)

sys.stderr = FilteredStderr()

# ---------------------------
# 📦 Importar TensorFlow (CPU)
# ---------------------------
import tensorflow as tf

# ---------------------------
# 🔢 Inicialización de tensores
# ---------------------------
tensor1 = tf.constant(4, shape=(1, 1), dtype=tf.float32)
tensor2 = tf.constant([[1, 2, 3], [4, 5, 6]])
tensor3 = tf.ones((3, 3))
tensor4 = tf.zeros((2, 3))
tensor5 = tf.eye(3)
tensor6 = tf.random.normal((3, 3), mean=0, stddev=1)
tensor7 = tf.random.uniform((1, 3), minval=0, maxval=1)
tensor8 = tf.range(start=1, limit=10, delta=2)
tensor9 = tf.cast(tensor8, dtype=tf.float64)

# ---------------------------
# 🖨️ Mostrar tensores
# ---------------------------
print("Tensor con valores aleatorios (distribución normal):")
print(tensor6)
print("----------")
print(tensor7)
print("----------")
print(tensor8)
print("----------")
print(tensor9)

# ---------------------------
# ➕ Operaciones matemáticas
# ---------------------------
x = tf.constant([1, 2, 3])
y = tf.constant([9, 8, 7])

z = tf.add(x, y)
z = tf.subtract(x, y)
z = tf.divide(x, y)
z = tf.multiply(x, y)

# Producto escalar (dot product)
z = tf.tensordot(x, y, axes=1)
print("Producto escalar:", z.numpy())

# Potencias
z = x ** 5
print("x elevado a 5:", z.numpy())

# Multiplicación de matrices
x = tf.random.normal((2, 3))
y = tf.random.normal((3, 4))
z = tf.matmul(x, y)
print("Multiplicación de matrices:")
print(z)

z = x @ y
print(z)
print("-----")
print("-----")
print("-----")
# Indexing

x = tf.constant([0,1,1,2,3,1,2,3])
print(x[:])