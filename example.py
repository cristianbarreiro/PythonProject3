import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import warnings
warnings.filterwarnings('ignore', category=UserWarning)

# Redirección avanzada para ocultar cualquier 'WARNING:tensorflow' de stderr
import sys
import io

class FilteredStderr(io.StringIO):
    def write(self, s):
        if "WARNING:tensorflow" not in s:
            sys.__stderr__.write(s)

sys.stderr = FilteredStderr()

# Ahora sí importamos TensorFlow
import tensorflow as tf

# ---------------------------
# 🔢 Inicialización de tensores
# ---------------------------

# Constante escalar 4 (1x1)
tensor1 = tf.constant(4, shape=(1, 1), dtype=tf.float32)

# Matriz constante 2x3
tensor2 = tf.constant([[1, 2, 3], [4, 5, 6]])

# Matriz de unos (3x3)
tensor3 = tf.ones((3, 3))

# Matriz de ceros (2x3)
tensor4 = tf.zeros((2, 3))

# Matriz identidad (3x3)
tensor5 = tf.eye(3)

# Matriz con valores aleatorios con distribución normal (media 0, desviación 1)
tensor6 = tf.random.normal((3, 3), mean=0, stddev=1)

# ---------------------------
# 🖨️ Mostrar un tensor
# ---------------------------

print("Tensor con valores aleatorios (distribución normal):")
print(tensor6)
