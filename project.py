import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Forzar uso solo CPU
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'   # Suprimir logs

import warnings
warnings.filterwarnings('ignore', category=UserWarning)
import sys
import io

class FilteredStderr(io.StringIO):
    def write(self, s):
        if "WARNING:tensorflow" not in s:
            sys.__stderr__.write(s)
sys.stderr = FilteredStderr()

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist

# Listar GPUs (normalmente vacío porque forzamos CPU)
physical_devices = tf.config.list_physical_devices('GPU')

if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
else:
    print("⚠️ No se detectó GPU, usando CPU.")

# Cargar MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28*28).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28*28).astype("float32") / 255.0

x_train = tf.convert_to_tensor(x_train, dtype="float32")

print("x_train tensor shape:", x_train.shape)
print("Primer vector de entrada (flatten 28x28):")
print(x_train[0].numpy())  # muestra el vector de 784 valores normalizados

# Sequential API (Very convenient, not very flexible)

