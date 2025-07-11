import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # ⚠️ No usar GPU

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Asegurar ejecución eager (modo default en TF 2.x)
tf.config.run_functions_eagerly(True)

# Cargar datos
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar a [0,1] y codificar etiquetas
x_train = x_train / 255.0
x_test = x_test / 255.0
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Modelo simple
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compilar y entrenar
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=32, verbose=1)

# Evaluar
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\n🔍 Accuracy: {acc*100:.2f}%")
