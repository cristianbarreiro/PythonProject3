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

model = keras.Sequential(
    [
        layers.Dense(512, activation="relu"),
        layers.Dense(256, activation="relu"),
        layers.Dense(10),
    ]
)

model = keras.Sequential()
model.add(keras.Input(shape=(784)))
model.add(layers.Dense(512, activation="relu"))
model.add(layers.Dense(256, activation="relu"))
model.add(layers.Dense(10))

model = keras.Model(inputs=model.inputs, outputs=[model.layers[-2].output])
feature = model.predict(x_train)

print(feature.shape
      )
#print(model.summary())
import sys
sys.exit()
#Functional API (a bit more flexible)

inputs = keras.Input(shape=(784))
x = layers.Dense(512, activation="relu", name="first_layer")(inputs)
x = layers.Dense(256, activation="relu", name="second_layer")(x)
outputs = layers.Dense(10, activation="softmax")(x)
model = keras.Model(inputs=inputs, outputs=outputs)

#import sys
#sys.exit()

# noinspection PyUnreachableCode
model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(lr=0.001),
    metrics=["accuracy"],
)

model.fit(x_train, y_train, batch_size=32, epochs=5, verbose=2)
model.evaluate(x_test, y_test, batch_size=32, verbose=2)